import os

from celery import Celery
from django.apps import apps 
from django.conf import settings
from datetime import timedelta
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OpenGov.settings')

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
    'candidate-data-17th-term-loksabha-crontab': {
        'task': 'candidate data 17th term loksabha',
        'schedule': crontab(hour=16, minute=0),
        
    },
    'bills-data-crontab': {
        'task': 'bills_data',
        'schedule': crontab(hour=7, minute=30),
        
    },
    'debates-data-17th-crontab': {
        'task': 'debates_data',
        'schedule': crontab(hour=16, minute=0),
        
    },
    'question-data-17th-term-crontab': {
        'task': 'Question_data_17th_term',
        'schedule': crontab(hour=16, minute=0),
    },
    'attendance-data-17th-term': {
        'task': 'Attendance_data_17th_term',
        'schedule': crontab(hour=16, minute=0),
    },
    'asset-data-17th-term':{
        'task': 'Asset_data_17th_term',
        'schedule': crontab(hour=16, minute=0),
    },
    'candidate_data_16th_and_15th_term': {
        'task': 'Candidate_data_16th_and_15th_term',
        'schedule': crontab(hour=16, minute=0),
    },
    'question-data-16th-term': {
        'task': 'Question_data_16th term',
        'schedule': crontab(hour=16, minute=0),
    },
    'debates-data-16th-term': {
        'task': 'Debates_data_16th_term',
        'schedule': crontab(hour=16, minute=0),
    },
    'question-data-15th-term': {
        'task': 'Question_data_15th_term',
        'schedule': crontab(hour=16, minute=0),
    },
    'debates-data-15th-term': {
        'task': 'Debate_data_15th_term',
        'schedule': crontab(hour=16, minute=0),
    },
    'rajyasabha-candidate-data':{
        'task': 'Rajyasabha_candidate_data',
        'schedule': crontab(hour=16, minute=0),
    },
    'rajyasabha-question-data': {
        'task': 'Rajyasabha_question_data',
        'schedule': crontab(hour=16, minute=0),
    },


}
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

