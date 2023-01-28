from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # the image will be uploaded to MEDIA_ROOT / profilePic
    img = models.ImageField(default="profilePic/default.jpg", upload_to="profilePic")

    def __str__(self):
        return self.user.username + " Profile"

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        image = Image.open(self.img.path)

        if image.height > 300 or image.width > 300:
            image.thumbnail((300,300))
            image.save(self.img.path)
