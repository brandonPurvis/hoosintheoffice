from django.shortcuts import render
from hoosin import forms
from hoosin import models


def default(request):
    context = {}
    context.update({'search_form': forms.SearchForm()})
    context.update({'update_form': models.HoursEntryModelForm()})
    context.update({'entry_count': len(models.HoursEntry.objects.all())})
    return render(request, 'hoos/main.html', context=context)
