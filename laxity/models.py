from django.db import models
from django.db.models.deletion import CASCADE
from patient_profile.models import PatientProfile


class Laxity(models.Model):
    
    laxity_positive_points = models.CharField(max_length=200)
    mandibular_manipulation = models.CharField(max_length=200)
    premature_contact_point = models.CharField(max_length=200)
    max_opening = models.CharField(max_length=200)
    mandibular_opening_deviation = models.CharField(max_length=200)
    laterality = models.CharField(max_length=200)
    condylar_mobility = models.CharField(max_length=200)
    articulary_noises = models.CharField(max_length=200)
    presuntive_dx_articular = models.CharField(max_length=200)
    diagnose = models.CharField(max_length=200)
    treatment_plan = models.CharField(max_length=200)
    budget = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(PatientProfile, on_delete=CASCADE)

    def __str__(self):
        return self.diagnose
