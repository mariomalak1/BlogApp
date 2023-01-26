from django.shortcuts import render
from . import models
from django.contrib.auth.views import login_required
# Create your views here.

def homePage(request):
	posts = models.Post.objects.all()
	context = {"posts" : posts}
	return render(request, "blog/homepage.html", context)

def about(request):
	return render(request, "blog/about.html")