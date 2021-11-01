from django.forms import ModelForm
from .models import Laxity


class LaxityForm(ModelForm):
    class Meta:
        model = Laxity
        fields = ['laxity_positive_points', 'mandibular_manipulation', 'premature_contact_point', 'max_opening', 'mandibular_opening_deviation',
                  'laterality', 'condylar_mobility', 'articulary_noises', 'presuntive_dx_articular', 'diagnose', 'treatment_plan', 'budget', 'note', 'patient']
