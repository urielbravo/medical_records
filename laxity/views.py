from django.shortcuts import render, get_object_or_404, redirect
from .forms import LaxityForm
from .models import Laxity
from patient_profile.models import PatientProfile
from django.contrib.auth.decorators import login_required


def create_laxity(request, patient_pk):
    patient = PatientProfile.objects.get(pk=patient_pk)
    patient_laxity_studies = Laxity.objects.filter(patient__pk=patient_pk)

    context = {
        'patient_laxity_studies': patient_laxity_studies, 
        'patient': patient, 
        'succes_msg': "test de laxitud registrado exitosamente!",
        'form': LaxityForm,
    }

    if request.method == 'GET':
        return render(request, 'laxity/laxity_form.html', context)
    else:
        try:
            form = LaxityForm(request.POST)
            form.save()
            return render(request, 'laxity/laxity_list.html', context)
        except ValueError:
            context['error'] = 'formato equivocado'
            return render(request, 'laxity/laxity_form.html', context)


def list_laxity(request, patient_pk):
    patient = PatientProfile.objects.get(pk=patient_pk)
    patient_laxity_studies = Laxity.objects.filter(patient__pk=patient_pk)
    context = {
        'patient_laxity_studies': patient_laxity_studies, 
        'patient': patient
    }

    return render(request, 'laxity/laxity_list.html', context)


@login_required(login_url='loginuser')
def delete_laxity(request, laxity_pk, patient_pk):
    laxity = get_object_or_404(Laxity, pk=laxity_pk)
    if request.method == 'POST':
        laxity.delete()
        patient = PatientProfile.objects.get(pk=patient_pk)
        patient_laxity_studies = Laxity.objects.filter(patient__pk=patient_pk)
        context = {
        'patient_laxity_studies': patient_laxity_studies, 
        'patient': patient,
        'deleted_msg': 'Test eliminado'
        }
        return render(request, 'laxity/laxity_list.html', context)


@login_required(login_url='loginuser')
def laxity_detail(request, laxity_pk):
    laxity = get_object_or_404(Laxity, pk=laxity_pk)
    return render(request, 'laxity/laxity_detail.html', {'laxity': laxity})
