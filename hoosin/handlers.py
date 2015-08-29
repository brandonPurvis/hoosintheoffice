from hoosin import models

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def handle_new_hours_forms(data):
    professor = data['professor']
    course = data['course']

    hour_dict = {}
    for day in DAYS:
        hour_dict[day] = (data[day+'_start'], data[day+'_stop'])

    hours = ''
    for day, ends in hour_dict.iteritems():
        if any(ends):
            hours += day[:2] + '({}-{})'.format(ends[0].hour, ends[1].hour)

    new_entry = models.HoursEntry(
        professor=professor,
        course=course,
        hours=hours,
    )
    new_entry.save()
