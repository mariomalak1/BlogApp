from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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


@login_required
def accountView(request):
    # current_user = get_object_or_404(User, id = int(pk))
    return render(request, "user/account.html")