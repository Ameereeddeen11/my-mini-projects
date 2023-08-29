from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="profile")
    profile_pic = models.ImageField(default="unkown-profile.jpg", upload_to="images/profile-pic", blank=True)
    bio_user = models.TextField(max_length=150, blank=True)