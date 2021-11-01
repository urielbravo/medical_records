from django.forms import ModelForm, fields
from .models import Orthodontic


class OrthodonticForm(ModelForm):
    class Meta:
        model = Orthodontic
        fields = ['facial_profile', 'molar_class', 'canine_class', 'crossbite', 'habits', 'note', 'patient']