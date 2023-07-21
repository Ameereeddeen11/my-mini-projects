from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(upload_to="images/profile-pic/", default="unkown-profile.jpg", blank=True)
    bio_user = models.TextField(max_length=150, blank=True)