from django.db import models
from django.db.models.deletion import CASCADE
from patient_profile.models import PatientProfile


class MusclePalpation(models.Model):
    masseter_right = models.BooleanField(default=False)
    masseter_left = models.BooleanField(default=False)
    temporalis_right = models.BooleanField(default=False)
    temporalis_left = models.BooleanField(default=False)
    ecm_right = models.BooleanField(default=False)
    ecm_left = models.BooleanField(default=False)
    digastric_right = models.BooleanField(default=False)
    digastric_left = models.BooleanField(default=False)
    occipital_right = models.BooleanField(default=False)
    occipital_left = models.BooleanField(default=False)
    pc_right = models.BooleanField(default=False)
    pc_left = models.BooleanField(default=False)
    trapezius_right = models.BooleanField(default=False)
    trapezius_left = models.BooleanField(default=False)

    created_at = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(PatientProfile, on_delete=CASCADE)

    def __str__(self):
        return self.created_at

# Masetero
# Temporal
# ECM
# Digastrico
# Occipital
# PC
# Trapecio
