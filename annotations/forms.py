from django.forms import ModelForm, fields
from .models import Annotation


class AnnotationForm(ModelForm):
    class Meta:
        model = Annotation
        fields = ['title', 'body', 'patient']
