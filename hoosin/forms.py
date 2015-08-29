from django import forms
from hoosin import models

class SearchForm(forms.Form):
    query = forms.CharField()


class SubmitInfoForm(forms.ModelForm):
    class Meta:
        model = models.HoursEnrty
        exclude = []
