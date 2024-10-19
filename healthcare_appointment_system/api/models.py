
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
    name = models.CharField(max_length=100,default='Asimo')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    availability = models.JSONField() 
    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100,default='Asimo')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()  
    date_of_birth = models.DateField()  
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])  
    medical_history = models.TextField()
    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    status = models.CharField(max_length=20, default='Scheduled')
    # choices=[('scheduled','Scheduled'),
    #          ('completed', 'Completed')]

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    record_details = models.TextField(default='No details available')
    notes = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

class Prescription(models.Model):
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescriptions')
    medications = models.TextField()
    dosage = models.CharField(max_length=100)
    def __str__(self):
        return f'Prescription for {self.Patient} by {self.doctor}'


class Bill(models.Model):
    Patient = models.ForeignKey(Patient, on_delete= models.CASCADE, related_name='bills')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=[('paid', 'Paid'), ('pending', 'Pending')], default='pending')
    def __str__(self):
        return f'Bill for {self.Patient} - Amount: {self.amount} - Status: {self.status}'


