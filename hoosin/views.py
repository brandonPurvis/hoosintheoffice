from django.http import HttpResponse
from django.shortcuts import render

from hoosin import forms
from hoosin import models
from hoosin import handlers


def default(request):
    all_entries = models.HoursEntry.objects.all()
    context = {}
    context.update({'search_form': forms.SearchForm()})
    context.update({'update_form': forms.NewHoursForm()})
    context.update({'entry_count': len(all_entries)})
    context.update({'entries': all_entries})
    return render(request, 'hoos/main.html', context=context)


def new_hours_submission_hook(request):
    assert request.method == 'POST'
    hours_form = forms.NewHoursForm(request.POST)
    if hours_form.is_valid():
        form_data = hours_form.cleaned_data
        handlers.handle_new_hours_forms(form_data)
        return HttpResponse('Thanks')
    return HttpResponse('Invalid')
