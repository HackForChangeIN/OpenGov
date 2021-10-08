from celery import shared_task
from django.conf import settings
from OpenGov.celery import app

@shared_task(name = 'first_screening_reminder')
def first_screening_reminder():
    pass
