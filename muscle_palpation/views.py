from django.shortcuts import render, get_object_or_404, redirect
from .forms import MusclePalpationForm
from .models import MusclePalpation
from patient_profile.models import PatientProfile
from django.contrib.auth.decorators import login_required


def create_muscle_palpation(request, patient_pk):
    patient = PatientProfile.objects.get(pk=patient_pk)
    patient_muscle_palpations = MusclePalpation.objects.filter(patient__pk=patient_pk)

    context = {
        'patient_muscle_palpations': patient_muscle_palpations, 
        'patient': patient, 
        'succes_msg': "examen ortodontico registrado exitosamente!",
        'form': MusclePalpationForm,
    }

    if request.method == 'GET':
        return render(request, 'muscle_palpation/muscle_palpation_form.html', context)
    else:
        try:
            form = MusclePalpationForm(request.POST)
            form.save()
            return render(request, 'muscle_palpation/muscle_palpation_list.html', context)
        except ValueError:
            context['error'] = 'formato equivocado'
            return render(request, 'muscle_palpation/muscle_palpation_form.html', context)


def list_muscle_palpation(request, patient_pk):
    patient = PatientProfile.objects.get(pk=patient_pk)
    patient_muscle_palpations = MusclePalpation.objects.filter(patient__pk=patient_pk)
    context = {
        'patient_muscle_palpations': patient_muscle_palpations, 
        'patient': patient
    }

    return render(request, 'muscle_palpation/muscle_palpation_list.html', context)


@login_required(login_url='loginuser')
def delete_muscle_palpation(request, palpation_pk, patient_pk):
    muscle_palpation = get_object_or_404(MusclePalpation, pk=palpation_pk)
    if request.method == 'POST':
        muscle_palpation.delete()
        patient = PatientProfile.objects.get(pk=patient_pk)
        patient_muscle_palpations = MusclePalpation.objects.filter(patient__pk=patient_pk)
        context = {
        'patient_muscle_palpations': patient_muscle_palpations, 
        'patient': patient,
        'deleted_msg': 'Examen eliminado'
        }
        return render(request, 'muscle_palpation/muscle_palpation_list.html', context)


@login_required(login_url='loginuser')
def muscle_palpation_detail(request, palpation_pk):
    muscle_palpation = get_object_or_404(MusclePalpation, pk=palpation_pk)
    return render(request, 'muscle_palpation/muscle_palpation_detail.html', {'muscle_palpation': muscle_palpation})
