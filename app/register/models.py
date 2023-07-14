from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="recept")
    profile_pic = models.ImageField(upload_to="images/profile-pic/")
    #follow = models.ManyToManyField(User)