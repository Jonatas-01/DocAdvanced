from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import ProfileCreationForm


def my_home(request):
    """
    Render the home page
    """
    return render(request, "index.html")


def registration(request):
    """
    Render the registration page
    Ensures the user will be registred only if the form is submited and
    it pass the validation
    """
    if request.method == "POST":
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user) # log the user in

            if user.role == 'patient':
                return redirect("patient-form")
            elif user.role == 'doctor':
                return redirect("doctor-form")
            
            # add message confirmation
            return redirect("home")
    else:
        form = ProfileCreationForm()
    return render(request, "authentication/register.html", {"form": form})


def logout_view(request):
    """
    Render a log out page
    Ensures the user will log out only if the form is submited
    """
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return render(request, "authentication/logout.html")


def login_view(request):
    """
    Render the login page
    Ensures the user log in only if the form is submited and pass the
    validation.
    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.add_message(request, messages.ERROR,
                                 "Invalid username or password")

    return render(request, "authentication/login.html")
