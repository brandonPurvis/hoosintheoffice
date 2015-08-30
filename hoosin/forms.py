from django import forms


def build_text_form_control_widget(place_holder=None):
    return forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder':  place_holder or ''
    })


class SearchForm(forms.Form):
    query = forms.CharField(widget=build_text_form_control_widget('Search'))


class NewHoursForm(forms.Form):
    professor = forms.CharField(max_length=50, widget=build_text_form_control_widget('Professor'))
    course = forms.CharField(max_length=50, widget=build_text_form_control_widget('Course'))
    office = forms.CharField(max_length=50, widget=build_text_form_control_widget('Office'))

    monday_start = forms.TimeField(required=False, widget=build_text_form_control_widget('start'))
    monday_stop = forms.TimeField(required=False, widget=build_text_form_control_widget('end'))

    tuesday_start = forms.TimeField(required=False, widget=build_text_form_control_widget('start'))
    tuesday_stop = forms.TimeField(required=False, widget=build_text_form_control_widget('end'))

    wednesday_start = forms.TimeField(required=False, widget=build_text_form_control_widget('start'))
    wednesday_stop = forms.TimeField(required=False, widget=build_text_form_control_widget('end'))

    thursday_start = forms.TimeField(required=False, widget=build_text_form_control_widget('start'))
    thursday_stop = forms.TimeField(required=False, widget=build_text_form_control_widget('end'))

    friday_start = forms.TimeField(required=False, widget=build_text_form_control_widget('start'))
    friday_stop = forms.TimeField(required=False, widget=build_text_form_control_widget('end'))

    saturday_start = forms.TimeField(required=False, widget=build_text_form_control_widget('start'))
    saturday_stop = forms.TimeField(required=False, widget=build_text_form_control_widget('end'))

    sunday_start = forms.TimeField(required=False, widget=build_text_form_control_widget('start'))
    sunday_stop = forms.TimeField(required=False, widget=build_text_form_control_widget('end'))
