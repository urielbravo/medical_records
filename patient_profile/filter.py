import django_filters
from .models import PatientProfile

class PatientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = PatientProfile
        fields = ['name']
