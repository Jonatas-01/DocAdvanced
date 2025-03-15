from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PatientDetails, DoctorDetails
from .forms import PatientlDetailsForm, DoctorDetailsForm


@login_required
def patient_details_form(request):
    """
    Display the form to patients that registered in website
    Ensures the page will only be accessed by patients hat have not filled
    the personal details form yet
    Ensures to handle form submition only if the method is POST
    """
    if request.user.role != 'patient':
        messages.error(request, "Only patients has access to this page.")
        return redirect('home')
    
    if PatientDetails.objects.filter(user=request.user).exists():
        messages.add_message(request, messages.ERROR, "You have been filled this form already.")
        return redirect('account-details')

    if request.method == 'POST':
        form = PatientlDetailsForm(request.POST)
        if form.is_valid():
            patient_details = form.save(commit=False)
            patient_details.user = request.user
            patient_details.save()
            return redirect('home')
    else:
        form = PatientlDetailsForm()

    return render(request, "forms/patient_form.html", {'form': form})


@login_required
def doctor_details_form(request):
    """
    Display the form to doctor that registered in website
    Ensures the page will only be accessed by doctors that have not filled
    the personal details form yet
    Ensures to handle form submition only if the method is POST
    """
    if request.user.role != 'doctor':
        messages.error(request, "Only patients have access to this page.")
        return redirect('home')
    
    if DoctorDetails.objects.filter(user=request.user).exists():
        messages.add_message(request, messages.ERROR, "You have been filled this form already.")
        return redirect('account-details')

    if request.method == 'POST':
        form = DoctorDetailsForm(request.POST)
        if form.is_valid():
            doctor_details = form.save(commit=False)
            doctor_details.user = request.user
            doctor_details.save()
            return redirect('home')
    else:
        form = DoctorDetailsForm()

    return render(request, "forms/doctor_form.html", {'form': form})


@login_required
def account_view(request):
    """
    Display user details based on their role or redirect to the appropriate form.
    """
    details_model = PatientDetails if request.user.role == 'patient' else DoctorDetails

    if not details_model.objects.filter(user=request.user).exists():
        messages.add_message(
            request, messages.ERROR, "Unauthorized access. Please fill out your Personal Details Form first."
        )
        return redirect('patient-form' if request.user.role == 'patient' else 'doctor-form')

    template = "accounts/patient_details.html" if request.user.role == 'patient' else "accounts/doctor_details.html"
    details = get_object_or_404(details_model, user=request.user)

    return render(request, template, {'details': details})


@login_required
def edit_details(request):
    """
    Allow users to edit their personal details based on their role or redirect to the appropriate form.
    """
    details_model = PatientDetails if request.user.role == 'patient' else DoctorDetails

    if not details_model.objects.filter(user=request.user).exists():
        messages.add_message(
            request, messages.ERROR, "Unauthorized access. Please fill out your Personal Details Form first."
        )
        return redirect('patient-form' if request.user.role == 'patient' else 'doctor-form')
    
    if request.user.role == 'patient':
        details = get_object_or_404(PatientDetails, user=request.user)
        form_details = PatientlDetailsForm
        template = "forms/edit_patient_details.html"
    else:
        details = get_object_or_404(DoctorDetails, user=request.user)
        form_details = DoctorDetailsForm
        template = "forms/edit_doctor_details.html"

    if request.method == 'POST':
        form = form_details(request.POST, instance=details)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your details have been updated successfully.")
            return redirect('account-details')
    else:
        form = form_details(instance=details)
    
    return render(request, template, {'form': form})