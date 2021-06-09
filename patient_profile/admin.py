from django.contrib import admin
from .models import PatientProfile

class PatientProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


admin.site.register(PatientProfile, PatientProfileAdmin)
