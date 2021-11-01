from django.forms import ModelForm, fields
from .models import MusclePalpation


class MusclePalpationForm(ModelForm):
    class Meta:
        model = MusclePalpation
        fields = [
            'masseter_right',
            'masseter_left',
            'temporalis_right',
            'temporalis_left',
            'ecm_right',
            'ecm_left',
            'digastric_right',
            'digastric_left',
            'occipital_right',
            'occipital_left',
            'pc_right',
            'pc_left',
            'trapezius_right',
            'trapezius_left',
            'note',
            'patient'
        ]
