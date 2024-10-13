from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
from .models import Doctor, Patient, Appointment, MedicalRecord,Prescription,Bill
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, MedicalRecordSerializer,PrescriptionSerializer,BillSerializer
import logging
from .Permissions import *
logger = logging.getLogger(__name__)
class DoctorViewSet(viewsets.ModelViewSet):
    logger.error("hello")
    queryset = Doctor.objects.all()

    serializer_class = DoctorSerializer
    # permission_classes = [IsDoctor]
                     
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    # permission_classes = [IsPatient]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    # permission_classes = [IsAuthenticated]

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    # permission_classes = [IsAuthenticated]
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    # permission_classes = [permissions.IsAuthenticated]
class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer