from django.db import models
from django.db.models.deletion import CASCADE
from patient_profile.models import PatientProfile


class Annotation(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(PatientProfile, on_delete=CASCADE)

    def __str__(self):
        return self.title
