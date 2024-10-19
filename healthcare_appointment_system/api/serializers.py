from rest_framework import serializers
from .models import Doctor, Patient, Appointment, MedicalRecord,Bill,Prescription,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'role']
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'email', 'phone_number', 'address', 'date_of_birth', 'gender', 'medical_history']  

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        
        fields = ['id', 'Patient', 'amount', 'paid', 'status']
        extra_kwargs = {
            'status': {'required': False}}
        
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value

    def validate(self, attrs):
        if attrs.get('paid') and attrs.get('amount') > 0:
            raise serializers.ValidationError("Paid bills should have an amount of zero.")
        return attrs


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        
        fields = ['id', 'Patient', 'doctor', 'medications', 'dosage', 'created_at']
        read_only_fields = ['created_at']