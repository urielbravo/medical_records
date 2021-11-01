from django.db import models
from django.db.models.deletion import CASCADE
from patient_profile.models import PatientProfile


class Orthodontic(models.Model):
    facial_profile = models.CharField(max_length=200)
    molar_class = models.CharField(max_length=200)
    canine_class = models.CharField(max_length=200)
    crossbite = models.CharField(max_length=200)
    habits = models.CharField(max_length=200)
    note = models.TextField(max_length=500, blank=True )
    
    created_at = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(PatientProfile, on_delete=CASCADE)

    def __str__(self):
        return self.facial_profile
