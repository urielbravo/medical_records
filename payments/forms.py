from django.forms import ModelForm, fields
from .models import Payment


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['procedure_description', 'amount', 'patient']
