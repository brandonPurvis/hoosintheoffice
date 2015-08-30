from django.http import HttpResponse
from django.shortcuts import render

from hoosin import forms
from hoosin import models
from hoosin import handlers


def default(request, entries=None):
    if not entries:
        all_entries = models.HoursEntry.objects.all()
    else:
        all_entries = entries
    all_entries = [entry for entry in all_entries]
    all_entries = sorted(all_entries, key=lambda x: x.professor)

    context = {}
    context.update({'search_form': forms.SearchForm()})
    context.update({'entry_count': len(all_entries)})
    context.update({'entries': all_entries})
    return render(request, 'hoos/main.html', context=context)


def go_to_office_hours_form(request):
    context = {}
    context.update({'update_form': forms.NewHoursForm()})
    return render(request, 'hoos/new_hours_form.html', context=context)


def new_hours_submission_hook(request):
    assert request.method == 'POST'
    hours_form = forms.NewHoursForm(request.POST)
    if hours_form.is_valid():
        form_data = hours_form.cleaned_data
        handlers.handle_new_hours_forms(form_data)
        return HttpResponse('Thanks')
    return HttpResponse('Invalid')


def search_hook(request):
    assert request.method == 'POST'
    query_form = forms.SearchForm(request.POST)
    if query_form.is_valid():
        form_data = query_form.cleaned_data
        results = handlers.search(form_data)
        return default(request, entries=results)
    return HttpResponse('Invalid Query')
