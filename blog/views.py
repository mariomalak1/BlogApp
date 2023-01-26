from django.shortcuts import render
from . import models
# Create your views here.


def homePage(request):
	posts = models.Post.objects.all()
	context = {"posts" : posts}
	return render(request, "blog/homepage.html", context)