from django.http import HttpResponse
from django.shortcuts import render
from hoosin import forms
from hoosin import models

def default(request):
    context = {}
    context.update({'search_form': forms.SearchForm()})
    context.update({'update_form': forms.SubmitInfoForm()})
    context.update({'entry_count': len(models.HoursEnrty.objects.all())})
    return render(request, 'hoos/main.html', context=context)
