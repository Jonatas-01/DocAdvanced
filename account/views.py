from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PatientDetails, DoctorDetails
from .forms import PatientlDetailsForm, DoctorDetailsForm


@login_required
def patient_details_form(request):
    """
    Handle patient details form submission and display.
    This view function manages the patient details form, 
    allowing patients to submit their details.
    It includes authorization checks and prevents duplicate submissions.
    Args:
        request: HTTP request object containing user and form data
    Returns:
        HttpResponse: Rendered form page or redirect response
    Raises:
        None
    Flow:
        1. Checks if user is a patient, redirects to home if not
        2. Checks for existing details, redirects if already submitted
        3. Processes POST request and saves form data if valid
        4. Displays empty form for GET requests
    """
    if request.user.role != 'patient':
        messages.error(request, "Only patients has access to this page.")
        return redirect('home')

    if PatientDetails.objects.filter(user=request.user).exists():
        messages.add_message(request, messages.ERROR,
                             "You have been filled this form already.")
        return redirect('account-details')

    if request.method == 'POST':
        form = PatientlDetailsForm(request.POST)
        if form.is_valid():
            patient_details = form.save(commit=False)
            patient_details.user = request.user
            patient_details.save()
            return redirect('account-details')
    else:
        form = PatientlDetailsForm()

    return render(request, "forms/patient_form.html", {'form': form})


@login_required
def doctor_details_form(request):
    """
    View function for handling the doctor details form submission.
    This view is responsible for:
    1. Ensuring only doctors can access the form
    2. Preventing duplicate form submissions
    3. Processing and saving doctor details
    Args:
        request: HTTP request object containing user and form data
    Returns:
        - Redirect to 'home' if user is not a doctor
        - Redirect to 'account-details' if form already submitted or 
          successful submission
        - Rendered doctor_form.html with form if GET request or invalid form
    Raises:
        No explicit exceptions raised
    """
    if request.user.role != 'doctor':
        messages.error(request, "Only patients have access to this page.")
        return redirect('home')

    if DoctorDetails.objects.filter(user=request.user).exists():
        messages.add_message(request, messages.ERROR,
                             "You have been filled this form already.")
        return redirect('account-details')

    if request.method == 'POST':
        form = DoctorDetailsForm(request.POST)
        if form.is_valid():
            doctor_details = form.save(commit=False)
            doctor_details.user = request.user
            doctor_details.save()
            return redirect('account-details')
    else:
        form = DoctorDetailsForm()

    return render(request, "forms/doctor_form.html", {'form': form})


@login_required
def account_view(request):
    """
    This view handles displaying user account details for both 
    patients and doctors.
    It checks if the user has completed their profile details 
    and redirects to the appropriate form if not. If details exist,
    it renders the corresponding template.
    Args:
        request: HttpRequest object containing user information and metadata
    Returns:
        HttpResponse: Rendered template with user details
        HttpResponseRedirect: Redirect to form page if details don't exist
    Raises:
        Http404: If user details are not found for existing profile
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
    Handle the editing of user details for both patients and doctors.
    This view function allows users to edit their personal details 
    based on their role (patient or doctor). It ensures users 
    have existing details before allowing edits
    and redirects to appropriate forms if details don't exist.
    Args:
        request: The HTTP request object containing user and form data.
    Returns:
        HttpResponse: Rendered form page for editing details or redirect to:
            - account-details page on successful update
            - patient/doctor form page if no existing details found
    Raises:
        Http404: If the requested user details do not exist.
    Notes:
        - Determines the correct model and form based on user role
        - Validates submitted form data
        - Displays success/error messages using Django messages framework
        - Uses different templates for patients and doctors
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
            messages.add_message(request, messages.SUCCESS,
                                 "Your details have been updated successfully.")
            return redirect('account-details')
    else:
        form = form_details(instance=details)

    return render(request, template, {'form': form})
