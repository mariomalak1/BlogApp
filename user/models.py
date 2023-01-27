from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # the image will be uploaded to MEDIA_ROOT / profilePic
    img = models.ImageField(default="profilePic/default.jpg", upload_to="profilePic")

    def __str__(self):
        return self.user.username + " Profile"