from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы подписались на рассылку',
        'ОК',
        'raixter04@gmail.com',
        [user_email],
        fail_silently=False,
    )