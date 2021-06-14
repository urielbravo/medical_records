from django.contrib import admin
from .models import Orthodontic

class OrthodonticAdmin(admin.ModelAdmin):
    list_display = ('facial_profile', 'molar_class', 'canine_class', 'patient')


admin.site.register(Orthodontic, OrthodonticAdmin)
