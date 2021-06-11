from django.db import models
from django.db.models.deletion import CASCADE
from patient_profile.models import PatientProfile


class Payment(models.Model):
    procedure_description = models.CharField(max_length=250)
    date_of_payment = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    patient = models.ForeignKey(PatientProfile, on_delete=CASCADE)

    def __str__(self):
        return self.procedure_description
