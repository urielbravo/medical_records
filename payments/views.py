from django.shortcuts import render, get_object_or_404
from .forms import PaymentForm
from .models import Payment
from patient_profile.models import PatientProfile
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

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


def list_payment(request,  patient_pk):
    total_payments = Payment.objects.filter(patient__pk=patient_pk).aggregate(Sum('amount'))
    user = PatientProfile.objects.get(pk=patient_pk)
    user_payments = Payment.objects.filter(patient__pk=patient_pk)
    return render(request, 'payment/payment_list.html', {'user_payments': user_payments, 'user': user, 'total_payments': total_payments})


@login_required(login_url='loginuser')
def delete_payment(request, payment_pk, patient_pk):
    payment = get_object_or_404(Payment, pk=payment_pk)
    if request.method == 'POST':
        payment.delete()
        user = PatientProfile.objects.get(pk=patient_pk)
        user_payments = Payment.objects.filter(patient__pk=patient_pk)
        total_payments = Payment.objects.filter(patient__pk=patient_pk).aggregate(Sum('amount'))
        context = {
        'user_payments': user_payments, 
        'user': user,
        'total_payments': total_payments,
        'deleted_msg': 'Pago eliminado'
        }
        return render(request, 'payment/payment_list.html', context)


def all_payments(request):
    total_payments = Payment.objects.all().aggregate(Sum('amount'))
    all_payments = Payment.objects.all()
    context = {
        'all_payments': all_payments,
        'total_payments': total_payments
    }
    return render(request, 'payment/all_payments.html', context)
