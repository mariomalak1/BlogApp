from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account have been created for {username}!")
            return redirect("home-page")
    else:
        form = UserRegistrationForm()
    return render(request, "user/register.html", {"form":form})