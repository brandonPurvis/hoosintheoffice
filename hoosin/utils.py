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
