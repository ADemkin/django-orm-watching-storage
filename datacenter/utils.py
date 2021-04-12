from datetime import timedelta

from django.utils.timezone import localtime


def get_visit_duration(visit):
  if visit.leaved_at is None:
    # if not yet leaved count current visit duration
    return localtime() - visit.entered_at
  return visit.leaved_at - visit.entered_at


def duration_to_human_readable(duration):
    '''format timedelta as HHH:MM:SS string'''
    seconds_total = duration.total_seconds()
    return '{hours:d}:{minutes:02d}:{seconds:02d}'.format(
      hours=int(seconds_total // 60 // 60 % 24),
      minutes=int(seconds_total // 60 % 60),
      seconds=int(seconds_total % 60),
    )


def is_visit_suspicious(visit, allowed_minutes=60):
  allowed_time = timedelta(minutes=allowed_minutes)
  return get_visit_duration(visit) > allowed_time
