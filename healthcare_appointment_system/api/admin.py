from django.contrib import admin
from .models import User  
# Register your models here.

from .models import User,Patient, Doctor, Appointment, MedicalRecord, Prescription, Bill

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('Patient', 'doctor', 'dosage')
    search_fields = ('Patient__name', 'doctor__name')
class BillAdmin(admin.ModelAdmin):
    list_display = ('Patient', 'amount', 'paid', 'status')
    list_filter = ('paid', 'status')
    search_fields = ('Patient__name',)
class CustomAdminSite(admin.AdminSite):
    site_header = 'Healthcare Admin Panel'
    site_title = 'Healthcare Admin'
    index_title = 'Welcome to the Healthcare Admin Panel'

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(Prescription, PrescriptionAdmin)
admin.site.register(Bill, BillAdmin)




