from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	title = models.CharField(max_length = 100)
	content = models.TextField()
	date_create = models.DateTimeField(default = timezone.now)
	date_edited = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("home-page")