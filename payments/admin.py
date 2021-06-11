from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('date_of_payment',)
    list_display = ('procedure_description', 'patient', 'date_of_payment', 'amount')


admin.site.register(Payment, PaymentAdmin)
