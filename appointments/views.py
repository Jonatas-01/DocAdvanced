from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import DoctorDetails, PatientDetails
from .models import Appointment
from .forms import AppointmentRequestForm


@login_required
def appointments_patient_view(request):
    """
    Handle patient's appointment management operations.
    This view allows patients to manage their appointments including viewing, canceling, 
    editing and deleting appointments. It displays appointments categorized by their status
    (pending, confirmed, rejected/canceled).
    Args:
        request: HttpRequest object containing metadata about the request
    Returns:
        HttpResponse: Rendered template with appointments data or redirect response
        after appointment actions
    Raises:
        Http404: If requested appointment or patient details are not found
    Notes:
        - Only accessible to users with 'patient' role
        - Supports POST actions for: cancel, edit, and delete appointments
        - Provides list of all available doctors
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
                    request, 
                    f"Your appointment with Dr. {appointment.doctor.first_name} has been updated.")
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
    Handle doctor's appointment view and actions.
    This view function manages a doctor's appointments, including viewing pending,
    confirmed, and rejected/canceled appointments. It also handles various appointment
    actions like confirmation, rejection, editing, cancellation, and deletion.
    Args:
        request: HttpRequest object containing metadata about the request
    Returns:
        HttpResponse: Renders the doctor's appointment view template with appointment lists
        or redirects to appropriate pages after actions
    Raises:
        Http404: If the doctor details are not found for the logged-in user
    Access Control:
        - Only accessible to users with 'doctor' role
        - Redirects to home page if unauthorized user attempts access
    Actions Supported:
        - confirm: Confirms appointment with scheduled date
        - reject: Rejects the appointment
        - edit: Modifies appointment scheduled date
        - cancel: Cancels the appointment
        - delete: Removes the appointment from system
    """

    if request.user.role != 'doctor':
        messages.error(request, "Only doctor has access to this page.")
        return redirect('home')

    doctor = get_object_or_404(DoctorDetails, user=request.user)

    pending_appointments = Appointment.objects.filter(
        doctor=doctor, status="pending")
    confirmed_appointments = Appointment.objects.filter(
        doctor=doctor, status="confirmed")
    rejected_canceled_appointments = Appointment.objects.filter(
        doctor=doctor, status__in=['rejected', 'canceled'])

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
                    request, f'Appointment confirmed for {appointment.scheduled_date}'
                    f'with {appointment.patient.first_name} {appointment.patient.last_name}.')
                return redirect('appointments')
            else:
                messages.error(
                    request, "Please provide a valid date for confirmation.")
        elif action == 'reject':
            appointment.status = 'rejected'
            appointment.save()
            messages.warning(request, "Appointment has been rejected.")
            return redirect('appointments')
        elif action == 'edit':
            scheduled_date = request.POST.get('scheduled_date')
            if scheduled_date:
                appointment.scheduled_date = scheduled_date
                appointment.save()
                messages.success(
                    request, 
                    f"Your appointment with {appointment.patient.first_name} has been reschedule.")
                return redirect('appointments')
            else:
                messages.error(
                    request, "Please provide a valid date for confirmation.")
        elif action == 'cancel':
            appointment.status = 'canceled'
            appointment.save()
            messages.warning(
                request,
                f"Your appointment with Dr. {appointment.patient.first_name} has been canceled.")
            return redirect('appointments')
        elif action == 'delete':
            appointment.delete()
            messages.error(
                request,
                f"Your appointment with Dr. {appointment.patient.first_name} has been deleted.")
            return redirect('appointments')

    return render(request, "doctor/appointment_doctor_view.html", {
        'pending_appointments': pending_appointments,
        'confirmed_appointments': confirmed_appointments,
        'rejected_canceled_appointments': rejected_canceled_appointments,
    })


@login_required
def appointments_view(request):
    """
    Handle appointment views based on user role and authorization.
    This view function determines which appointment view to display based on the user's role
    (patient or doctor) and checks if the user has completed their personal details.
    Args:
        request: HttpRequest object containing metadata about the request
    Returns:
        HttpResponse: Redirects to:
            - patient/doctor appointment view if authorized and role matches
            - patient/doctor form if personal details are incomplete
            - home page if role is invalid
    Raises:
        No explicit exceptions are raised
    Note:
        - Users must have completed their personal details before accessing appointments
        - Only authenticated users with valid roles (patient/doctor) can access appointments
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
    Handle appointment requests from patients to doctors.
    This view function processes appointment requests, ensuring that:
    1. Only authenticated patients can request appointments
    2. Patients have completed their personal details
    3. The requested doctor exists
    Args:
        request: The HTTP request object
        doctor_id (int): The ID of the doctor to request an appointment with
    Returns:
        HttpResponse: Renders the appointment request form or redirects after submission
            - If successful: Redirects to appointments page with success message
            - If unauthorized: Redirects with error message
            - If GET: Renders request_appointment.html with form
    Raises:
        Http404: If the doctor or patient details are not found
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
