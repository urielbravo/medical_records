from django.contrib import admin
from .models import PainMapping

class PainMappingAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('created_at', 'patient')


admin.site.register(PainMapping, PainMappingAdmin)
