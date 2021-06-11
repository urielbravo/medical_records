from django.shortcuts import render
from .forms import PaymentForm
from .models import Payment
from patient_profile.models import PatientProfile
from django.db.models import Sum

# all the other regular functions
def create_payment(request, patient_pk):
    patient = PatientProfile.objects.get(pk=patient_pk)
    user = PatientProfile.objects.get(pk=patient_pk)
    user_payments = Payment.objects.filter(patient__pk=patient_pk)
    if request.method == 'GET':
        return render(request, 'payment/payment_form.html', {'form': PaymentForm, 'patient': patient})
    else:
        try:
            form = PaymentForm(request.POST)
            form.save()
            total_payments = Payment.objects.filter(patient__pk=patient_pk).aggregate(Sum('amount'))
            return render(request, 'payment/payment_list.html', {'user_payments': user_payments, 'user': user, 'succes_msg': "pago registrado exitosamente!", 'total_payments': total_payments})
        except ValueError:
            return render(request, 'payment/payment_form.html', {'form': PaymentForm, 'error': 'Bad Data passes in'})


def list_payment(request, patient_pk):
    total_payments = Payment.objects.filter(patient__pk=patient_pk).aggregate(Sum('amount'))
    user = PatientProfile.objects.get(pk=patient_pk)
    user_payments = Payment.objects.filter(patient__pk=patient_pk)
    return render(request, 'payment/payment_list.html', {'user_payments': user_payments, 'user': user, 'total_payments': total_payments})
