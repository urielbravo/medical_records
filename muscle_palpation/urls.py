from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:patient_pk>', views.create_muscle_palpation, name='create_muscle_palpation'),
    path('list/<int:patient_pk>', views.list_muscle_palpation, name='list_muscle_palpation'),
    path('delete/<int:palpation_pk>/<int:patient_pk>/', views.delete_muscle_palpation, name='delete_muscle_palpation'),
    path('detail/<int:palpation_pk>', views.muscle_palpation_detail, name='muscle_palpation_detail'),
]