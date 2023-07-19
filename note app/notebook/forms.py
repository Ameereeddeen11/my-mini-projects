from dataclasses import fields
from pyexpat import model
from django import forms
from .models import *

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "name",
            "text",
        ]

