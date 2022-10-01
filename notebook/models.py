from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime 

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="note_user")
    name = models.CharField(max_length=200)
    update = models.DateField()

class Block2(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    chat = models.TextField()
