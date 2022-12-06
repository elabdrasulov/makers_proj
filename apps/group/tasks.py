import datetime
from celery.schedules import crontab
from config.celery_ import app
from celery import shared_task
from django.utils import timezone
from rest_framework.response import Response

from apps.group.models import Group
from apps.room.models import Room

# app.conf.beat_schedule = {
#     # Выполнять ежедневно в полночь.
#     'add-every-day': {
#         'task': 'tasks.graduate_group',
#         'schedule': crontab(minute=0, hour=0),
#     },
# }

# @periodic_task(run_every=crontab(minute=0, hour=0))

@shared_task
def graduate_group():
    groups = Group.objects.all()
    today = datetime.date.today()
    for group in groups:
        if group.date_of_end:
            if group.date_of_end == today:
                group.is_graduated = True
                if group.group_studying_time == 'day':
                    group.mentor.mentor_status_day = False
                    group.room.room_status_day = False
                    for tracker in group.tracker.all():
                        tracker.mentor_status_day = False
                elif group.group_studying_time == 'evening':
                    group.mentor.mentor_status_evening = False
                    group.room.room_status_evening = False
                    for tracker in group.tracker.all():
                        tracker.mentor_status_evening = False
                group.save()
    return 'OK'
    
    # rooms = Room.objects.all()
    # for room in rooms:
    #     room.room_status_day = True
    #     room.save()
    # return 'OK'