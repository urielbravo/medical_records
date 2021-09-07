from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:patient_pk>', views.create_laxity, name='create_laxity'),
    path('list/<int:patient_pk>', views.list_laxity, name='list_laxity'),
    path('delete/<int:laxity_pk>/<int:patient_pk>/', views.delete_laxity, name='delete_laxity'),
    path('detail/<int:laxity_pk>', views.laxity_detail, name='laxity_detail'),
]