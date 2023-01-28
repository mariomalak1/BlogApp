from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.views import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreatePostForm
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, ListView, CreateView
# Create your views here.

# def homePage(request):
# 	posts = models.Post.objects.all()
# 	context = {"posts": posts}
# 	return render(request, "blog/homepage.html", context)

# using based view class not function
class PostViewList(ListView):
	model = models.Post
	context_object_name = "posts"
	ordering = "-date_create"
	# template search on <appName>/<modelName>_<genericViewName>

# this the running class view
class PostDetailView(DetailView):
	model = models.Post


def about(request):
	return render(request, "blog/about.html")

@login_required
def CreatePost(request):
	if request.method == "POST":
		form = CreatePostForm(request.POST)
		if form.is_valid():
			form.save()
			# post = models.Post(author=request.user, title=form.title, content=form.content)
			# post.save()
			messages.success(request, "post created successfully")
			return redirect("home-page")
	else:
		form = CreatePostForm()
		return render(request, "blog/post.html", {"form":form})

# class based view that is running now
class PostCreateView(LoginRequiredMixin,CreateView):
	model = models.Post
	template_name = "blog/post.html"  # "blog/post_create.html"
	fields = ["title", "content"]

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(UpdateView):
	model = models.Post
	template_name = "blog/post_edit.html"
	fields = ["title", "content"]

	def dispatch(self, request, *args, **kwargs):
		post = self.get_object()
		user_object = request.user
		if user_object != post.author:
			return redirect("postDetail", post.id)
		return super().dispatch(request, *args, **kwargs)