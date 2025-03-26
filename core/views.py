from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import ProfileCreationForm


def my_home(request):
    """
    Render the home page of the application.
    This view function handles the home page request and returns
    the rendered index.html template.
    Args:
        request: HttpRequest object containing metadata about the request
    Returns:
        HttpResponse: The rendered index.html template
    """
    return render(request, "index.html")


def registration(request):
    """
    Handle user registration process.
    This view function manages the registration of new users. It checks if the user
    is already authenticated, processes the registration form submission, and redirects
    users based on their role after successful registration.
    Args:
        request: HttpRequest object containing metadata about the request.
    Returns:
        HttpResponse: Redirects to appropriate page based on user role and authentication status.
                     - If user is authenticated: redirects to 'home'
                     - If registration successful: redirects to 'patient-form' or 'doctor-form' based on role
                     - If GET request: renders registration form
    """
    if request.user.is_authenticated:
        return redirect('home')
    
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
    Handle user logout functionality.
    This view processes the logout request and redirects to the login page.
    Args:
        request: HttpRequest object containing metadata about the request
    Returns:
        HttpResponse: Redirects to login page on POST request
        HttpResponse: Renders logout confirmation template on GET request
    """
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return render(request, "authentication/logout.html")


def login_view(request):
    """
    Handle user authentication and login process.
    This view function manages the login process for users. If the user is already
    authenticated, they are redirected to the home page. For POST requests, it
    attempts to authenticate the user with provided credentials and logs them in
    if successful. Otherwise, it displays an error message.
    Args:
        request: The HTTP request object containing user data and session information.
    Returns:
        HttpResponseRedirect: Redirects to 'home' if login is successful or user is
            already authenticated.
        HttpResponse: Renders login template if authentication fails or on GET request.
    Raises:
        None
    """
    if request.user.is_authenticated:
        return redirect('home')
    
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
