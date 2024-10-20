from django.contrib.admin import ModelAdmin  
from django.urls import path  
from django.shortcuts import render, redirect  
from .models import Patient  

class PatientAdmin(ModelAdmin):  
    list_display = ('name', 'phone_number', 'medical_history')  
    search_fields = ('name',)  

    def get_urls(self):  
        urls = super().get_urls()  
        custom_urls = [  
            path('add/', self.admin_site.admin_view(self.add_view), name='add_patient'),  
            path('list/', self.admin_site.admin_view(self.list_view), name='patient_list'),  
        ]  
        return custom_urls + urls  

    def add_view(self, request):  
        if request.method == 'POST':  
            # Handle the form submission here  
            name = request.POST.get('name')  
            phone_number = request.POST.get('phone_number')  
            medical_history = request.POST.get('medical_history')  
            Patient.objects.create(name=name, phone_number=phone_number, medical_history=medical_history)  
            return redirect('admin:api_patient_changelist')  # Redirect to patient list after adding  

        return render(request, 'admin/add_patient.html')  

    def list_view(self, request):  
        patients = Patient.objects.all()  
        return render(request, 'admin/patient_list.html', {'patients': patients})