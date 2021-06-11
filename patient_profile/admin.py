from django.contrib import admin
from .models import PatientProfile

class PatientProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'created_at', 'email', 'phone_number')


admin.site.register(PatientProfile, PatientProfileAdmin)
