import json

from django.db.models import Q

from hoosin import models
from hoosin import utils

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def handle_new_hours_forms(data):
    professor = data['professor']
    course = data['course']
    office = data['office']

    hour_dict = {}
    for day in DAYS:
        hour_dict[day] = (data[day+'_start'], data[day+'_stop'])
    hours = ''
    for day, ends in hour_dict.iteritems():
        if any(ends):
            hours += day[:2] + '({}:{}-{}:{});'.format(ends[0].hour, ends[0].minute,
                                                       ends[1].hour, ends[1].minute)

    new_entry = models.HoursEntry(
        professor=professor,
        course=course,
        hours=hours,
        office=office,
    )
    new_entry.save()


def new_handle_new_hours_form(data):
    professor = data['professor']
    course = data['course']
    office = data['office']

    hours = {}
    for i, day in enumerate(DAYS):
        ends = (data[day+'_start'], data[day+'_stop'])
        if any(ends):
            hours[i] = {
                'dow': day,
                'start': utils.time_to_str(data[day+'_start']),
                'end': utils.time_to_str(data[day+'_stop']),
            }
    pickled_hours = json.dumps(hours)
    models.NewHoursEntry(
        professor=professor,
        course=course,
        office=office,
        pickled_hours=pickled_hours,
    ).save()
    return True


def search(data):
    query = data['query']
    query = Q(professor__contains=query) | Q(course__contains=query)
    matches = models.NewHoursEntry.objects.filter(query)
    return matches
