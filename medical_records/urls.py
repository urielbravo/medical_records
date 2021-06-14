from django.contrib import admin
from django.urls import path, include
from patient_profile import views as patient_profile_views
from django.conf.urls.static import static
from django.conf import settings
from payments import views as payments_views


urlpatterns = [
    path('master/', admin.site.urls),

    # Auth
    path('login/', patient_profile_views.login_user, name='loginuser'),
    path('logout/', patient_profile_views.logout_user, name='logoutuser'),

    # Patient Profile
    path('', patient_profile_views.create_patient_profile, name='patient_profile'),

    # Administrator
    path('admin/', patient_profile_views.admin, name='admin'),
    path('patient/<int:patient_pk>', patient_profile_views.patient_detail, name='patient_detail'),
    path('patient/update/<int:patient_pk>', patient_profile_views.patient_update, name='patient_update'),
    path('patient/<int:patient_pk>/delete', patient_profile_views.patient_delete, name='patient_delete'),

    #Payments
    path('payment/create/<int:patient_pk>', payments_views.create_payment, name='create_payment'),
    path('payments/<int:patient_pk>', payments_views.list_payment, name='list_payment'),
    path('payment/delete/<int:payment_pk>/<int:patient_pk>/', payments_views.delete_payment, name='delete_payment'),
    path('payment/list/', payments_views.all_payments, name='all_payments'),

    #orthodontics urls
    path('orthdontics/', include('orthodontic.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
