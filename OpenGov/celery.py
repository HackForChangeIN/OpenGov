import os

from celery import Celery
from django.apps import apps 
from django.conf import settings
from datetime import timedelta
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HFC.settings')

app = Celery('OpenGov')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
#app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'
from celery.schedules import crontab
app.conf.beat_schedule = {
    'send-first-reminder-contrab': {
        'task': 'first_screening_reminder',
        'schedule': crontab(hour=6, minute=0),
        
    },
    'send-second-reminder-contrab': {
        'task': 'second_screening_reminder',
        'schedule': crontab(hour=6, minute=0),
        
    },
    'send-third-reminder-contrab': {
        'task': 'third_screening_reminder',
        'schedule': crontab(hour=6, minute=0),
        
    },
    
}
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

