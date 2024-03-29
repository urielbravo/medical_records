from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import REDIRECT_FIELD_NAME, login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import PatientProfileForm, PatientUpdateProfileForm
from .models import PatientProfile
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .filter import PatientFilter
from django.db.models.functions import ExtractYear


# functions to login a logout the user, basically the auth users
def login_user(request):
    if request.method == 'GET':
        return render(request, 'registration/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration/loginuser.html', {'form': AuthenticationForm(), 'error': 'Usuario y/o contraseña invalidos'})
        else:
            login(request, user)
            return redirect('admin')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginuser')


# all the other regular functions
@login_required(login_url='loginuser')
def create_patient_profile(request):
    if request.method == 'GET':
        return render(request, 'patient_profile/patient_form.html', {'form': PatientProfileForm})
    else:
        try:
            form = PatientProfileForm(request.POST)
            form.save()
            return render(request, 'patient_profile/patient_form.html', {'succes_msg': "perfil creado exitosamente! Gracias!"})
        except ValueError:
            return render(request, 'patient_profile/patient_form.html', {'form': PatientProfileForm, 'error': 'Bad Data passes in'})


# here is the dashboard, here goes the list of patients
@login_required(login_url='loginuser')
def admin(request):
    patients = PatientProfile.objects.order_by('-created_at')


    # Fiter by name of the patient functionality
    patient_filter = PatientFilter(request.GET, queryset=patients)
    patients = patient_filter.qs

    # Paginator functionality
    paginator = Paginator(patients, 15)
    page = request.GET.get('page')
    page_patients = paginator.get_page(page)

    # saving search value from the filter
    search_value = request.GET.get('name', '')
    print('value:', search_value)

    context = {
        'patients': page_patients,
        'patient_filter': patient_filter,
        'search_value': search_value
    }

    return render(request, 'admin/admin_dashboard.html', context)


@login_required(login_url='loginuser')
def patient_detail(request, patient_pk):
    patient = get_object_or_404(PatientProfile, pk=patient_pk)
    print('birthday', ExtractYear(patient.birthday))
    return render(request, 'admin/patient_detail.html', {'patient': patient})


@login_required(login_url='loginuser')
def patient_update(request, patient_pk):
    patient = get_object_or_404(PatientProfile, pk=patient_pk)
    if request.method == 'GET':
        form = PatientUpdateProfileForm(instance=patient)
        return render(request, 'admin/patient_update_form.html', {'patient': patient, 'form': form})
    else:
        try:
            form = PatientUpdateProfileForm(request.POST, request.FILES, instance=patient)
            form.save()
            return render(request, 'admin/patient_detail.html', {'patient': patient})
        except ValueError:
            return render(request, 'admin/patient_update_form.html', {'patient': patient, 'form': form, 'error': 'bad info'})


@login_required(login_url='loginuser')
def patient_delete(request, patient_pk):
    patient = get_object_or_404(PatientProfile, pk=patient_pk)
    if request.method == 'POST':
        patient.delete()
        patients = PatientProfile.objects.all()
        context = {
            'patients': patients,
            'user_deleted_msg': "User deleted"
        }
        return render(request, 'admin/admin_dashboard.html', context)
