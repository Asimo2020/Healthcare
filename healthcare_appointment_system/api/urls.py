
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, PatientViewSet, AppointmentViewSet, MedicalRecordViewSet, BillViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'medical-records', MedicalRecordViewSet)
router.register(r'Bill', BillViewSet)

urlpatterns = [
    path('', include(router.urls)),
]