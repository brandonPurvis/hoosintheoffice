from django.db import models
from django.forms import ModelForm


class HoursEntry(models.Model):
    professor = models.CharField(max_length=30)
    course = models.CharField(max_length=20)
    hours = models.CharField(max_length=100)


class HoursEntryModelForm(ModelForm):
    class Meta:
        model = HoursEntry
        fields = ['professor', 'course', 'hours']
