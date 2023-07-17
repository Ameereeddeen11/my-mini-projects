from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(upload_to="images/profile-pic/", null=True, default="unkown-profile.jpg")
    #follow = models.ManyToManyField(User)
    bio_user = models.TextField(max_length=200, null=True, blank=True)