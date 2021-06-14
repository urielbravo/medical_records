from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:patient_pk>', views.create_orthodontic, name='create_orthodontic'),
    path('list/<int:patient_pk>', views.list_orthodontic, name='list_orthodontic'),
    path('delete/<int:orthodontic_pk>/<int:patient_pk>/', views.delete_orthodontic, name='delete_orthodontic'),
]