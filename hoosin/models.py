import re
import datetime

from django.db import models
from django.forms import ModelForm

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


class HoursEntry(models.Model):
    professor = models.CharField(max_length=30)
    course = models.CharField(max_length=20)
    hours = models.CharField(max_length=100)

    @property
    def is_in_office(self):
        today = datetime.date.today()
        dow = today.weekday()
        day = DAYS[dow]
        pattern = '{}\((.+?)\)'.format(day[:2])
        pattern = re.compile(pattern)
        match = re.search(pattern, self.hours)
        if not match:
            return "No"
        start_hour, end_hour = map(int, match.group(1).split('-'))
        current_hour = datetime.datetime.now().hour
        in_office = (start_hour <= current_hour) and (current_hour <= end_hour)
        return 'Yes' if in_office else 'No'
