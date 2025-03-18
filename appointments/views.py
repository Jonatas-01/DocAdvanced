from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import DoctorDetails, PatientDetails
from .models import Appointment
from .forms import AppointmentRequestForm


@login_required
def appointments_patient_view(request):
    """
    Handles the view for patient appointments.
    This view performs the following actions:
    - Checks if the user has the 'patient' role. If not, redirects to the home page with an error message.
    - Retrieves the patient's details based on the logged-in user.
    - Fetches the patient's appointments categorized by their status: pending, confirmed, rejected, or canceled.
    - Retrieves all doctor details.
    - Handles POST requests to perform actions on appointments:
        - Cancel an appointment.
        - Edit an appointment's notes and set its status to pending.
        - Delete an appointment.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered HTML page for patient appointments.
    """

    if request.user.role != 'patient':
        messages.error(request, "Only patients has access to this page.")
        return redirect('home')

    patient = get_object_or_404(PatientDetails, user=request.user)

    pending_appointments = Appointment.objects.filter(
        patient=patient, status="pending")
    confirmed_appointments = Appointment.objects.filter(
        patient=patient, status="confirmed")
    rejected_canceled_appointments = Appointment.objects.filter(
        patient=patient, status__in=["rejected", "canceled"])

    doctors = DoctorDetails.objects.all()

    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        action = request.POST.get('action')

        appointment = get_object_or_404(
            Appointment, id=appointment_id, patient=patient)

        if action == 'cancel':
            appointment.status = 'canceled'
            appointment.save()
            messages.warning(request, "Appointment has been canceled.")
            return redirect('appointments')
        elif action == 'edit':
            notes = request.POST.get('notes')
            if notes:
                appointment.notes = notes
                appointment.status = "pending"
                appointment.save()
                messages.success(
                    request, f"Your appointment with Dr. {appointment.doctor.first_name} {appointment.doctor.last_name} has been updated.")
        elif action == 'delete':
            appointment.delete()
            messages.error(request, "Appointment has been deleted.")
            return redirect('appointments')

    return render(request, "patient/appointments_patient_view.html", {
        'doctors': doctors,
        'pending_appointments': pending_appointments,
        'confirmed_appointments': confirmed_appointments,
        'rejected_canceled_appointments': rejected_canceled_appointments,
    })


@login_required
def appointments_doctor_view(request):
    """

    """

    if request.user.role != 'doctor':
        messages.error(request, "Only doctor has access to this page.")
        return redirect('home')

    doctor = get_object_or_404(DoctorDetails, user=request.user)

    pending_appointments = Appointment.objects.filter(
        doctor=doctor, status="pending")
    confirmed_appointments = Appointment.objects.filter(
        doctor=doctor, status="confirmed")

    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        action = request.POST.get('action')

        appointment = get_object_or_404(
            Appointment, id=appointment_id, doctor=doctor)

        if action == 'confirm':
            scheduled_date = request.POST.get('scheduled_date')
            if scheduled_date:
                appointment.status = "confirmed"
                appointment.scheduled_date = scheduled_date
                appointment.save()
                messages.success(
                    request, f"Appointment confirmed for {appointment.scheduled_date} with {appointment.patient.first_name} {appointment.patient.last_name}.")
                return redirect('appointments')
            else:
                messages.error(
                    request, "Please provide a valid date for confirmation.")
                
        elif action == 'reject':
            appointment.status = 'rejected'
            appointment.save()
            messages.warning(request, "Appointment has been rejected.")
            return redirect('appointments')

    return render(request, "doctor/appointment_doctor_view.html", {
        'pending_appointments': pending_appointments,
        'confirmed_appointments': confirmed_appointments
    })


@login_required
def appointments_view(request):
    """

    """

    if not DoctorDetails.objects.filter(user=request.user).exists() and not PatientDetails.objects.filter(user=request.user).exists():
        messages.error(
            request, "Unauthorized access. Please fill out your Personal Details Form first.")
        return redirect('patient-form' if request.user.role == 'patient' else 'doctor-form')

    if request.user.role == 'patient':
        return appointments_patient_view(request)
    elif request.user.role == 'doctor':
        return appointments_doctor_view(request)

    return redirect('home')


@login_required
def request_appointment(request, doctor_id):
    """
    Handles the appointment request process for patients.
    This view function performs the following tasks:
    1. Checks if the user is a patient. If not, an error message is displayed and the user is redirected.
    2. Verifies if the patient's personal details are filled out. If not, an error message is displayed and the user is redirected.
    3. Retrieves the doctor and patient details based on the provided doctor_id and the logged-in user.
    4. If the request method is POST, it processes the appointment request form. If the form is valid, the appointment is saved and a success message is displayed.
    5. If the request method is not POST, it initializes the appointment request form with the doctor's details.
    Args:
        request (HttpRequest): The HTTP request object.
        doctor_id (int): The ID of the doctor for whom the appointment is being requested.
    Returns:
        HttpResponse: The rendered template with the appointment request form or a redirect response.
    """

    if request.user.role != 'patient':
        messages.error(request, "Only patients has access to this page.")
        return redirect('appointments')

    if not PatientDetails.objects.filter(user=request.user).exists():
        messages.add_message(
            request, messages.ERROR, "Unauthorized access. Please fill out your Personal Details Form first."
        )
        return redirect('patient-form')

    doctor = get_object_or_404(DoctorDetails, id=doctor_id)
    patient = get_object_or_404(PatientDetails, user=request.user)

    if request.method == 'POST':
        form = AppointmentRequestForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.doctor = doctor
            appointment.save()
            messages.add_message(
                request, messages.SUCCESS, f"Your appointment request with Dr. {doctor.first_name} {doctor.last_name} has been sent.")
            return redirect('appointments')
    else:
        form = AppointmentRequestForm(initial={'doctor': doctor})

    return render(request, "form/request_appointment.html", {'form': form, 'doctor': doctor})
