from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PatientlDetailsForm


@login_required
def patient_details_form(request):
    """
    Display the form to patients that registred in website
    Ensures the page will only be accessed by patients
    Ensures to handle form submition only if the method is POST
    """
    if request.user.role != 'patient':
        # display message here
        return redirect('home')

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
