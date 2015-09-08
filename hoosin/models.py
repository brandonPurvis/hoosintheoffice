import re
import datetime
import json

from django.db import models

from hoosin import utils

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


class HoursEntry(models.Model):
    professor = models.CharField(max_length=30)
    course = models.CharField(max_length=20)
    hours = models.CharField(max_length=100)
    office = models.CharField(max_length=50)

    @property
    def show_hours(self):
        return self.hours

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

    @property
    def calendar_url(self):
        url = "http://www.google.com/calendar/event?action=TEMPLATE"
        attrs = {
            'text': "{} Office hours".format(self.course),
            'dates': '20140127T224000Z/20140320T221500Z', # &dates=[start-custom format='Ymd\\THi00\\Z']/[end-custom format='Ymd\\THi00\\Z']
            'details': "Office hours for professor {} in {}".format(self.professor, self.office),
            'location': self.office,
            'trp': False,
            'sprop': '',
        }
        for key, value in attrs.iteritems():
            url += '&{}={}'.format(key, value)
        url = url.replace(' ', '+')
        return url


class NewHoursEntry(models.Model):
    professor = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    office = models.CharField(max_length=20)
    pickled_hours = models.TextField()

    @property
    def hours(self):
        un_pickled = json.loads(self.pickled_hours)
        return un_pickled

    @property
    def show_hours(self):
        s = ''
        hours = self.hours
        for i in range(7):
            if hours.get(str(i)):
                s += DAYS[i][:2]
                s += '({}-{})'.format(hours[str(i)]['start'], hours[str(i)]['end'])
        return s

    @property
    def is_in_office(self):
        now = utils.get_current_time()
        hours = self.hours

        todays_hours = hours.get(str(now.weekday()))
        if not todays_hours:
            return False
        todays_hours['start'] = utils.str_to_time(todays_hours['start']).time()
        todays_hours['end'] = utils.str_to_time(todays_hours['end']).time()
        return todays_hours['start'] <= now.time() <= todays_hours['end']

    @property
    def next_hours(self):
        now = utils.get_current_time()
        hours = self.hours

        days = hours.keys()

        next_day = 0
        while str((now.weekday() + next_day) % 7) not in days:
            next_day += 1

        next_day_of_week = (now.weekday() + next_day) % 7
        next_date = now + datetime.timedelta(days=next_day)

        hours = hours[str(next_day_of_week)]
        hours['start'] = utils.str_to_time(hours['start'])

        next_start = next_date.replace(
            hour=hours['start'].hour,
            minute=hours['start'].minute,
            second=0,
        )
        return next_start

    @property
    def calendar_url(self):
        next_hours = self.next_hours
        next_end = next_hours + datetime.timedelta(hours=1)

        start = next_hours.strftime('%Y%m%dT%H%M00Z')
        stop = next_end.strftime('%Y%m%dT%H%M00Z')
        time_string = '/'.join([start, stop])

        url = "http://www.google.com/calendar/event?action=TEMPLATE"
        attrs = {
            'text': "{} Office hours".format(self.course),
            'dates': time_string, # &dates=[start-custom format='Ymd\\THi00\\Z']/[end-custom format='Ymd\\THi00\\Z']
            'details': "Office hours for professor {} in {}".format(self.professor, self.office),
            'location': self.office,
            'trp': False,
            'sprop': '',
        }
        for key, value in attrs.iteritems():
            url += '&{}={}'.format(key, value)
        url = url.replace(' ', '+')
        return url
