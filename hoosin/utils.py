from datetime import datetime


def time_to_str(d):
    return d.strftime('%H:%M')

def str_to_time(s):
    return datetime.strptime(s, '%H:%M')
