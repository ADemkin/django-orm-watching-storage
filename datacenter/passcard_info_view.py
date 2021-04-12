from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datetime import timedelta

from .utils import get_visit_duration
from .utils import duration_to_human_readable
from .utils import is_visit_suspicious


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits = []
    for visit in Visit.objects.filter(
      passcard=passcard,
      leaved_at__isnull=False,
    ):
      this_passcard_visits.append(
        {
            'entered_at': visit.entered_at,
            'duration': duration_to_human_readable(
                get_visit_duration(visit),
            ),
            'is_strange': is_visit_suspicious(visit),
        },
      )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
