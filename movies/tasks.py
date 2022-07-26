from django_movies.celery import app
from .service import send
from django.core.mail import send_mail

from .models import Contact

@app.task
def send_spam_email(user_email):
    send(user_email)

@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Мы будем присылать вам много спама',
            f'Вы {contact.name}',
            'raixter04@gmail.com',
            [contact.email],
            fail_silently=False
        )