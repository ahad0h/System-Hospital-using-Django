from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Clinic
from django.db.models import Q
from .forms import PatientForm


def home(request):
    return render(request, 'ahad/home.html')


def patient_list(request):
    query = request.GET.get('q')
    patients = Patient.objects.all()

    if query:
        patients = patients.filter(
            Q(name__icontains=query) |
            Q(phone__icontains=query) |
            Q(clinic__name__icontains=query)
        )

    return render(request, 'ahad/patient_list.html', {'patients': patients})


def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'ahad/display.html', {'patient': patient})


def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()

    return render(request, 'ahad/add_patient.html', {'form': form})


def search_patients(request):
    query = request.GET.get('q')
    patients = []

    if query:
        patients = Patient.objects.filter(
            Q(name__icontains=query) |
            Q(phone__icontains=query) |
            Q(clinic__name__icontains=query)
        )

    return render(request, 'ahad/search.html', {
        'patients': patients,
        'query': query
    })
