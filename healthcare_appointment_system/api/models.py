
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin','Admin'),
        ('doctor','Doctor'),
        ('patient', 'Patient'),
    )
    role = models.CharField(max_length=10, choices= ROLE_CHOICES)
class Doctor(models.Model):
    user = models.OneToOneField('api.User', on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    availability = models.JSONField()  # Example: [{"day": "Monday", "slots": ["09:00", "10:00"]}, ...]

class Patient(models.Model):
    user = models.OneToOneField('api.User', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    medical_history = models.TextField()

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=20, default='Scheduled')
    choices=[('scheduled','Scheduled'),
             ('completed', 'Completed')]

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    notes = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

class Prescription(models.Model):
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medications = models.TextField()
    dosage = models.CharField(max_length=100)

class Bill(models.Model):
    Patient = models.ForeignKey(Patient, on_delete= models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

