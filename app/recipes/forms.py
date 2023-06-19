from django import forms 
from .models import *

class Recipe(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = [
            "title",
            "discription",
            "ingredient",
            "instructions",
            "category",
        ]