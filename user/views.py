from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm, UserUpdatedForm, ProfileUpdatedForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog import models as blog_Models
from .models import Profile
from django.contrib.auth import login as loginTheUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    all_post = blog_Models.Post.objects.filter(author__id=request.user.id).order_by("-date_create")
    page = request.GET.get('page', 1)
    posts_paginate = Paginator(all_post, 5)

    try:
        posts = posts_paginate.page(page)
    except PageNotAnInteger:
        posts = posts_paginate.page(1)
    except EmptyPage:
        posts = posts_paginate.page(paginator.num_pages)


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
        "posts": posts,
        "page_obj": posts,
        "paginator": posts_paginate
    }
    return render(request, "user/account.html", context)


@login_required
def accountAnotherView(request, pk):
    user_ = get_object_or_404(User,id = pk)
    all_post = blog_Models.Post.objects.filter(author_id = user_.id).order_by("-date_create")
    profile = get_object_or_404(Profile, user = user_)

    page = request.GET.get('page', 1)
    posts_paginate = Paginator(all_post, 2)

    try:
        posts = posts_paginate.page(page)
    except PageNotAnInteger:
        posts = posts_paginate.page(1)
    except EmptyPage:
        posts = posts_paginate.page(paginator.num_pages)

    context = {"user_":user_,
               "profile":profile,
               "posts":posts,
               "page_obj": posts,
               "paginator": posts_paginate
               }
    return render(request, "user/account_another.html", context)