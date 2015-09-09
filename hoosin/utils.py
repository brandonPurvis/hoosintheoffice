from datetime import datetime
from pytz import timezone


EST = timezone('US/Eastern')


def time_to_str(d):
    return d.strftime('%H:%M')


def str_to_time(s):
    return datetime.strptime(s, '%H:%M')


def get_current_time():
    return datetime.now(tz=EST)


def get_current_time_string():
    now = datetime.now(tz=EST)
    return now.strftime('%H:%M')


def datetime_to_google_string(d):
    year = d.year
    month = d.month
    day = d.day

    hour = d.hour + 4
    minute = d.minute

    s = '{}{:02}{:02}T{:02}{:02}00Z'.format(
        year,
        month,
        day,
        hour,
        minute
    )
    return s
