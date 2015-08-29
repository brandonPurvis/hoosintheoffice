from django import forms


class SearchForm(forms.Form):
    query = forms.CharField()


class NewHoursForm(forms.Form):
    professor = forms.CharField(max_length=50)
    course = forms.CharField(max_length=50)

    monday_start = forms.TimeField(required=False)
    monday_stop = forms.TimeField(required=False)

    tuesday_start = forms.TimeField(required=False)
    tuesday_stop = forms.TimeField(required=False)

    wednesday_start = forms.TimeField(required=False)
    wednesday_stop = forms.TimeField(required=False)

    thursday_start = forms.TimeField(required=False)
    thursday_stop = forms.TimeField(required=False)

    friday_start = forms.TimeField(required=False)
    friday_stop = forms.TimeField(required=False)

    saturday_start = forms.TimeField(required=False)
    saturday_stop = forms.TimeField(required=False)

    sunday_start = forms.TimeField(required=False)
    sunday_stop = forms.TimeField(required=False)
