import os
from celery import Celery, Task
from celery.schedules import crontab

from django.conf import settings

# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# you change the name here
app = Celery("config")

# read config from Django settings, the CELERY namespace would make celery 
# config keys has `CELERY` prefix
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    # Выполнять ежедневно в полночь.
    'add-every-day': {
        'task': 'apps.group.tasks.graduate_group',
        'schedule': crontab(minute=0, hour=0),
    },
}

# app.conf.beat_schedule = {
#     # Выполнять каждую минуту.
#     'every-1-minute': {
#         'task': 'apps.group.tasks.graduate_group',
#         'schedule': crontab(),
#     },
# }


# load tasks.py in django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)