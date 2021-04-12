from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


from .utils import get_visit_duration
from .utils import duration_to_human_readable
from .utils import is_visit_suspicious


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at=None):
      non_closed_visits.append(
        {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': duration_to_human_readable(
                get_visit_duration(visit),
            ),
            'is_strange': is_visit_suspicious(visit),
        },
      )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
