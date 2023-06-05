from django.db import models
from django.contrib.auth.models import User

class Recipes(models.Model):
    title = models.CharField(max_length=150)
    discription = models.TextField()
    instructions = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "f{self.title} - {self.discription} - {self.created_by.username}"
    
