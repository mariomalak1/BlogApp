from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, UserUpdatedForm, ProfileUpdatedForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog import models as blog_Models
from .models import Profile
from django.contrib.auth import login as loginTheUser
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account have been created for {username}!")
            user_ = User.objects.get(username= username)
            loginTheUser(request,user_)
            return redirect("account-view")
    else:
        form = UserRegistrationForm()
    return render(request, "user/register.html", {"form":form})


@login_required
def accountView(request):
    posts = blog_Models.Post.objects.filter(author__id = request.user.id)
    if request.method == "POST":
        userForm = UserUpdatedForm(request.POST, instance= request.user)
        profileForm = ProfileUpdatedForm(request.POST, request.FILES, instance=request.user.profile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect("account-view")
    else:
        userForm = UserUpdatedForm(instance= request.user)
        profileForm = ProfileUpdatedForm(instance=request.user.profile)

    context = {
        "userForm":userForm,
        "profileForm":profileForm,
        "posts":posts,
    }
    for post in posts:
        print(post.author)
    return render(request, "user/account.html", context)

def accountAnotherView(request, pk):
    user_ = get_object_or_404(User,id = pk)
    posts = blog_Models.Post.objects.filter(author_id = user_.id)
    profile = Profile.objects.get(user = user_)
    context = {"user_":user_, "profile":profile, "posts":posts}
    return render(request, "user/account_another.html", context)