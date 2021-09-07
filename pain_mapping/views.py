from django.shortcuts import render, get_object_or_404, redirect
from .forms import PainMappingForm
from .models import PainMapping
from patient_profile.models import PatientProfile
from django.contrib.auth.decorators import login_required


def create_pain_mapping(request, patient_pk):
    patient = PatientProfile.objects.get(pk=patient_pk)
    patient_pain_mapping_studies = PainMapping.objects.filter(patient__pk=patient_pk)

    context = {
        'patient_pain_mapping_studies': patient_pain_mapping_studies, 
        'patient': patient, 
        'succes_msg': "test de mapeo de dolor registrado!",
        'form': PainMappingForm,
    }

    if request.method == 'GET':
        return render(request, 'pain_mapping/pain_mapping_form.html', context)
    else:
        try:
            print('request.POST:', request.POST)
            form = PainMappingForm(request.POST)
            form.save()
            return render(request, 'pain_mapping/pain_mapping_list.html', context)
        except ValueError:
            context['error'] = 'formato equivocado'
            return render(request, 'pain_mapping/pain_mapping_form.html', context)


def list_pain_mapping(request, patient_pk):
    patient = PatientProfile.objects.get(pk=patient_pk)
    patient_pain_mapping_studies = PainMapping.objects.filter(patient__pk=patient_pk)
    context = {
        'patient_pain_mapping_studies': patient_pain_mapping_studies, 
        'patient': patient
    }

    return render(request, 'pain_mapping/pain_mapping_list.html', context)


@login_required(login_url='loginuser')
def delete_pain_mapping(request, pain_mapping_pk, patient_pk):
    pain_mapping = get_object_or_404(PainMapping, pk=pain_mapping_pk)
    if request.method == 'POST':
        pain_mapping.delete()
        patient = PatientProfile.objects.get(pk=patient_pk)
        patient_pain_mapping_studies = PainMapping.objects.filter(patient__pk=patient_pk)
        context = {
        'patient_pain_mapping_studies': patient_pain_mapping_studies, 
        'patient': patient,
        'deleted_msg': 'Test eliminado'
        }
        return render(request, 'pain_mapping/pain_mapping_list.html', context)

@login_required(login_url='loginuser')
def pain_mapping_detail(request, pain_mapping_pk):
    pain_mapping = get_object_or_404(PainMapping, pk=pain_mapping_pk)
    return render(request, 'pain_mapping/pain_mapping_detail.html', {'pain_mapping': pain_mapping})
