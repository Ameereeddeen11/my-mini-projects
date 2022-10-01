from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime 

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="note_user")
    name = models.CharField(max_length=200)
    text = models.TextField(null=True)
    update = models.DateField(auto_now_add=True, null=True)