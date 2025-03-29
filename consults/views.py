from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from appointments.models import Appointment
from account.models import DoctorDetails, PatientDetails
from .models import Consult


@login_required
def start_consult(request, appointment_id):
    """
    Start a medical consultation for a specific appointment.
    This view handles both GET and POST requests for creating
    a medical consultation.
    Only doctors are authorized to access this functionality. For POST
    requests, it creates a new consultation record with the provided
    medical information and closes the associated appointment.
    Args:
        request: The HTTP request object
        appointment_id (int): The ID of the appointment for the consultation
    Returns:
        GET: Renders the start_consult.html template with the
        appointment context
        POST: Redirects to the consults page after creating the consultation
    Raises:
        Http404: If the appointment with given ID does not exist
    Notes:
        Required POST parameters:
        - symptoms: Patient's symptoms
        - diagnosis: Doctor's diagnosis
        - prescription: Prescribed medications/treatment
        Optional POST parameters:
        - allergies: Patient's allergies
        - medications: Current medications
        - notes: Additional notes
    """
    if request.user.role != 'doctor':
        messages.error(request, "Only doctor has access to this page.")
        return redirect('consults')

    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        symptoms = request.POST.get('symptoms')
        allergies = request.POST.get('allergies')
        medications = request.POST.get('medications')
        diagnosis = request.POST.get('diagnosis')
        prescription = request.POST.get('prescription')
        notes = request.POST.get('notes')

        if not symptoms or not diagnosis or not prescription:
            messages.error(request, "Symptoms and diagnosis are required.")

        Consult.objects.create(
            appointment=appointment,
            symptoms=symptoms,
            allergies=allergies,
            medications=medications,
            diagnosis=diagnosis,
            prescription=prescription,
            notes=notes,
        )

        appointment.status = 'closed'
        appointment.save()

        messages.success(request, "Consult has been created.")
        return redirect('consults')

    return render(request, 'consults/start_consult.html', {'appointment': appointment})


@login_required
def edit_consult(request, consult_id):
    """
    Edit an existing consultation record.
    This view function allows doctors to modify the details of an
    existing consultation.
    Only users with the 'doctor' role can access this functionality.
    Args:
        request: The HTTP request object.
        consult_id (int): The ID of the consultation to edit.
    Returns:
        HttpResponse: Renders the edit consultation form on GET requests.
        HttpResponseRedirect: Redirects to consults list page after
        successful update on POST requests.
    Raises:
        Http404: If the consultation with given ID does not exist.
    Notes:
        - Checks if user has doctor role before allowing access
        - Updates the following fields: symptoms, allergies, medications,
        diagnosis, prescription, notes
        - Shows success message after successful update
    """
    if request.user.role != 'doctor':
        messages.error(request, "Only doctor has access to this page.")
        return redirect('consults')

    consult = get_object_or_404(Consult, id=consult_id)

    if request.method == 'POST':
        consult.symptoms = request.POST.get('symptoms')
        consult.allergies = request.POST.get('allergies')
        consult.medications = request.POST.get('medications')
        consult.diagnosis = request.POST.get('diagnosis')
        consult.prescription = request.POST.get('prescription')
        consult.notes = request.POST.get('notes')
        consult.save()

        messages.success(request, "Consult updated successfully.")
        return redirect('consults')

    return render(request, 'consults/edit_consult.html', {'consult': consult})


@login_required
def consults_view(request):
    """
    View function for handling consult-related operations.
    This view handles both GET and POST requests for consults. For GET requests,
    it displays consults based on the user's role (doctor or patient). For POST
    requests, it handles consult deletion.
    Args:
        request: HttpRequest object containing metadata about the request
    Returns:
        HttpResponse: Renders consults_view.html template with consults data
        HttpResponseRedirect: Redirects to appropriate form if profile
        is incomplete or to consults page after deletion
    Raises:
        Http404: If the requested consult for deletion doesn't exist
    Notes:
        - For doctors: shows consults related to their appointments
        - For patients: shows consults related to their appointments
        - Requires user authentication and completed profile
        - Orders consults by creation date (newest first)
    """
    consults = None

    if request.user.role == 'doctor':
        if not DoctorDetails.objects.filter(user=request.user).exists():
            messages.error(
                request, 'Please complete your doctor profile first.')
            return redirect('doctor-form')
        else:
            doctor = DoctorDetails.objects.get(user=request.user)
            consults = Consult.objects.filter(
                appointment__doctor=doctor
            ).order_by('-created_at')
    elif request.user.role == 'patient':
        if not PatientDetails.objects.filter(user=request.user).exists():
            messages.error(
                request, 'Please complete your patient profile first.')
            return redirect('patient-form')
        else:
            patient = PatientDetails.objects.get(user=request.user)
            consults = Consult.objects.filter(
                appointment__patient=patient
            ).order_by('-created_at')

    if request.method == 'POST':
        consult_id = request.POST.get('consult_id')
        consult = get_object_or_404(Consult, id=consult_id)
        consult.delete()
        messages.error(request, "Your consult has been deleted.")
        return redirect('consults')

    return render(request, 'consults/consults_view.html', {'consults': consults})
