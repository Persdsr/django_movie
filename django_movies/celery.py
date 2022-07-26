from celery import Celery
import os

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_movies.settings')

app = Celery('django_movies')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-spam-every-5-minute': {
        'task': 'movies.tasks.send_beat_email',
        'schedule': crontab(minute='*/5')
    },
}

#celery -A send_email worker -l info -P eventlet
