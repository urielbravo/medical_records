import orthodontic
from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrthodonticForm
from .models import Orthodontic
from patient_profile.models import PatientProfile
from django.contrib.auth.decorators import login_required


def create_orthodontic(request, patient_pk):
    patient = PatientProfile.objects.get(pk=patient_pk)
    patient_orthodontics = Orthodontic.objects.filter(patient__pk=patient_pk)

    context = {
        'patient_orthodontics': patient_orthodontics, 
        'patient': patient, 
        'succes_msg': "examen ortodontico registrado exitosamente!",
        'form': OrthodonticForm,
    }

    if request.method == 'GET':
        return render(request, 'orthodontic/orthodontic_form.html', context)
    else:
        try:
            form = OrthodonticForm(request.POST)
            form.save()
            return render(request, 'orthodontic/orthodontic_list.html', context)
        except ValueError:
            context['error'] = 'formato equivocado'
            return render(request, 'orthodontic/orthodontic_form.html', context)


def list_orthodontic(request, patient_pk):
    patient = PatientProfile.objects.get(pk=patient_pk)
    patient_orthodontics = Orthodontic.objects.filter(patient__pk=patient_pk)
    context = {
        'patient_orthodontics': patient_orthodontics, 
        'patient': patient
    }

    return render(request, 'orthodontic/orthodontic_list.html', context)


@login_required(login_url='loginuser')
def delete_orthodontic(request, orthodontic_pk, patient_pk):
    orthodontic = get_object_or_404(Orthodontic, pk=orthodontic_pk)
    if request.method == 'POST':
        orthodontic.delete()
        patient = PatientProfile.objects.get(pk=patient_pk)
        patient_orthodontics = Orthodontic.objects.filter(patient__pk=patient_pk)
        context = {
        'patient_orthodontics': patient_orthodontics, 
        'patient': patient,
        'deleted_msg': 'Examen eliminado'
        }
        return render(request, 'orthodontic/orthodontic_list.html', context)
