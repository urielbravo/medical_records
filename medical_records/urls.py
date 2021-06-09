from django.contrib import admin
from django.urls import path
from patient_profile import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('master/', admin.site.urls),

    # Auth
    path('login/', views.login_user, name='loginuser'),
    path('logout/', views.logout_user, name='logoutuser'),

    # Patient Profile
    path('', views.create_patien_profile, name='patien_profile'),

    # Administrator
    path('admin/', views.admin, name='admin'),
    path('patient/<int:patient_pk>', views.patient_detail, name='patient_detail'),
    path('patient/update/<int:patient_pk>', views.patient_update, name='patient_update'),
    path('patient/<int:patient_pk>/delete', views.patient_delete, name='patient_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
