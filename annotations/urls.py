from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:patient_pk>', views.create_annotation, name='create_annotation'),
    path('list/<int:patient_pk>', views.list_annotations, name='list_annotations'),
    path('delete/<int:annotation_pk>/<int:patient_pk>/', views.delete_annotation, name='delete_annotation'),
]