import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'health_booking.settings')
app = Celery('health_booking')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()