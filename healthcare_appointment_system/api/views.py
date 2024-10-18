from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Doctor, Patient, Appointment, MedicalRecord,Prescription,Bill
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer, MedicalRecordSerializer,PrescriptionSerializer,BillSerializer
import logging
from .Permissions import *
logger = logging.getLogger(__name__)
class DoctorViewSet(viewsets.ModelViewSet):
    logger.error("hello")
    queryset = Doctor.objects.all()

    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]
                     
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated]
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]
class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['Patient', 'paid', 'status']
    ordering_fields = ['amount', 'created_at']
   