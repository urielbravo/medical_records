from django.shortcuts import render, get_object_or_404
from .forms import AnnotationForm
from .models import Annotation
from patient_profile.models import PatientProfile
from django.contrib.auth.decorators import login_required


@login_required(login_url='loginuser')
def create_annotation(request, patient_pk):
    patient = PatientProfile.objects.get(pk=patient_pk)
    patient_annotations = Annotation.objects.filter(patient__pk=patient_pk)

    context = {
        'patient_annotations': patient_annotations, 
        'patient': patient, 
        'succes_msg': "anotacion registrado exitosamente!",
        'form': AnnotationForm,
        'error': 'Datos mal entrados'
    }

    if request.method == 'GET':
        return render(request, 'annotations/annotations_form.html', context)
    else:
        try:
            form = AnnotationForm(request.POST)
            form.save()
            return render(request, 'annotations/annotations_list.html', context)
        except ValueError:
            return render(request, 'annotations/annotations_form.html', context)


@login_required(login_url='loginuser')
def list_annotations(request,  patient_pk):
    patient = PatientProfile.objects.get(pk=patient_pk)
    patient_annotations = Annotation.objects.filter(patient__pk=patient_pk)

    context = {
        'patient_annotations': patient_annotations, 
        'patient': patient
    }

    return render(request, 'annotations/annotations_list.html', context)


@login_required(login_url='loginuser')
def delete_annotation(request, annotation_pk, patient_pk):
    annotation = get_object_or_404(Annotation, pk=annotation_pk)
    if request.method == 'POST':
        annotation.delete()
        patient = PatientProfile.objects.get(pk=patient_pk)
        patient_annotations = Annotation.objects.filter(patient__pk=patient_pk)

        context = {
        'patient_annotations': patient_annotations, 
        'patient': patient,
        'deleted_msg': 'Anotacion eliminada'
        }

        return render(request, 'annotations/annotations_list.html', context)
