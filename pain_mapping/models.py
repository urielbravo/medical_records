from django.db import models
from django.db.models.deletion import CASCADE
from patient_profile.models import PatientProfile


class PainMapping(models.Model):
    right_side_pain_1 = models.PositiveSmallIntegerField(default=0)
    right_side_pain_2 = models.PositiveSmallIntegerField(default=0)
    right_side_pain_3 = models.PositiveSmallIntegerField(default=0)
    right_side_pain_4 = models.PositiveSmallIntegerField(default=0)
    right_side_pain_5 = models.PositiveSmallIntegerField(default=0)
    right_side_pain_6 = models.PositiveSmallIntegerField(default=0)
    right_side_pain_7 = models.PositiveSmallIntegerField(default=0)
    right_side_pain_8 = models.PositiveSmallIntegerField(default=0)
    left_side_pain_1 = models.PositiveSmallIntegerField(default=0)
    left_side_pain_2 = models.PositiveSmallIntegerField(default=0)
    left_side_pain_3 = models.PositiveSmallIntegerField(default=0)
    left_side_pain_4 = models.PositiveSmallIntegerField(default=0)
    left_side_pain_5 = models.PositiveSmallIntegerField(default=0)
    left_side_pain_6 = models.PositiveSmallIntegerField(default=0)
    left_side_pain_7 = models.PositiveSmallIntegerField(default=0)
    left_side_pain_8 = models.PositiveSmallIntegerField(default=0)
    note = models.TextField(max_length=500, blank=True )
    
    created_at = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(PatientProfile, on_delete=CASCADE)

    def __str__(self):
        return self.created_at
