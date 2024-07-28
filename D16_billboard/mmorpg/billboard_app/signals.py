from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMultiAlternatives
from .models import UserResponse, Advertisement
from django.template.loader import render_to_string
from django.conf import settings



def send_notifications_advert(pk, title, user_email):

    html_content = render_to_string(
        'callboard/advert_created_email.html',
    )
    print(user_email)
    to_emails = [user_email]
    msg = EmailMultiAlternatives(subject=title,  body='', from_email=settings.DEFAULT_FROM_EMAIL, bcc=to_emails)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

def send_notifications_responce(pk, title, user_email):

    html_content = render_to_string(
        'callboard/advert_created_email.html',
    )
    print(user_email)
    to_emails = [user_email]
    msg = EmailMultiAlternatives(subject=title,  body='', from_email=settings.DEFAULT_FROM_EMAIL, bcc=to_emails)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

@receiver(post_save, sender=Advertisement)
def advert_created(instance, created, **kwargs):
            if not created:
                return
            # print(instance.user)
            send_notifications_advert(instance.pk, instance.subject, instance.user)

@receiver(post_save, sender=UserResponse)
def responce_created(instance, created, **kwargs):
            if not created:
                return
            # print(instance.user)
            send_notifications_responce(instance.pk, instance.subject, instance.user)

@receiver(post_save, sender=UserResponse)
def my_handler(sender, instance, **kwargs):
            if instance.status:
                mail = instance.commentator.email
                send_mail(
                        subject='Подтверждение отклика',
                        message='Ваш отклик приняли)',
                        from_email='sunny.yanachka@mail.ru',
                        recipient_list=[mail],
                        fail_silently=False,
                      )

            else:
                    mail = instance.advertisement.author.email
                    send_mail(
                        subject='Подтверждение отклика',
                        message='Подтвердите получение отклика',
                        from_email='sunny.yanachka@mail.ru',
                        recipient_list=[mail],
                        fail_silently=False,
                    )