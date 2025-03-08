from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ProfileCreationForm


def my_home(request):
    """
    """
    return render(request, "index.html")


def registration(request):
    if request.method == "POST":
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("home")
    else:
        form = ProfileCreationForm()
    return render(request, "registration/register.html", {"form": form})
