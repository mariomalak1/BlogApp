from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.views import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CreatePostForm
from django.contrib import messages
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView
from django.utils import timezone
# from django
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
	paginate_by = 7
	# template search on <appName>/<modelName>_<genericViewName>

# this the running class view
class PostDetailView(LoginRequiredMixin, DetailView):
	model = models.Post


def about(request):
	return render(request, "blog/about.html")

# @login_required
# def CreatePost(request):
# 	if request.method == "POST":
# 		form = CreatePostForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			# post = models.Post(author=request.user, title=form.title, content=form.content)
# 			# post.save()
# 			messages.success(request, "post created successfully")
# 			return redirect("home-page")
# 	else:
# 		form = CreatePostForm()
# 		return render(request, "blog/post_create.html", {"form":form})

# class based view that is running now


class PostCreateView(LoginRequiredMixin,CreateView):
	model = models.Post
	template_name = "blog/post_create.html"  # "blog/post_create.html"
	fields = ["title", "content"]

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
	model = models.Post
	template_name = "blog/post_edit.html"
	fields = ["title", "content"]



	def form_valid(self, form):
		form.instance.date_edited = timezone.now()
		return super().form_valid(form)

	# this function to check on the logic of the view if you want
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False



	## old method to make sure that the current user that he will make the update request
	## , but note that he get the detail page instead of he gets 403 error

	# def dispatch(self, request, *args, **kwargs):
	# 	post = self.get_object()
	# 	user_object = request.user
	# 	if user_object != post.author:
	# 		return redirect("postDetail", post.id)
	# 	return super().dispatch(request, *args, **kwargs)



class PostDeleteView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
	model = models.Post
	template_name = "blog/delete_confirmation.html"

	# this function to check on the logic of the view if you want
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

	success_url = "/"
