from django.shortcuts import render
from hoosin import forms
from hoosin import models


def default(request):
    test_enrty = models.HoursEntry(professor='Joe Testum', course='TST 2102', hours='MWF:10-1,2-3,4-5')
    test_enrty.save()

    context = {}
    context.update({'search_form': forms.SearchForm()})
    context.update({'update_form': models.HoursEntryModelForm()})
    context.update({'entry_count': len(models.HoursEntry.objects.all())})
    return render(request, 'hoos/main.html', context=context)
