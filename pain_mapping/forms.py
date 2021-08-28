from django.forms import ModelForm
from .models import PainMapping


class PainMappingForm(ModelForm):
    class Meta:
        model = PainMapping
        fields = ['right_side_pain_1', 'right_side_pain_2', 'right_side_pain_3', 'right_side_pain_4', 'right_side_pain_5',
                  'right_side_pain_6', 'right_side_pain_7', 'right_side_pain_8', 'left_side_pain_1',
                  'left_side_pain_2', 'left_side_pain_3', 'left_side_pain_4', 'left_side_pain_5',
                  'left_side_pain_6', 'left_side_pain_7', 'left_side_pain_8'
                  ]
