from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:patient_pk>', views.create_pain_mapping, name='create_pain_mapping'),
    path('list/<int:patient_pk>', views.list_pain_mapping, name='list_pain_mapping'),
    path('delete/<int:pain_mapping_pk>/<int:patient_pk>/', views.delete_pain_mapping, name='delete_pain_mapping'),
]