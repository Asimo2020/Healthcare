from celery import shared_task
from django.core.mail import send_mail
from .models import Appointment

@shared_task
def send_appointment_reminder(appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    send_mail(
        'یادآوری نوبت',
        f'یادآوری: نوبت شما در {appointment.appointment_time}',
        'from@example.com',
        [appointment.patient.user.email],
        fail_silently=False,
    )
