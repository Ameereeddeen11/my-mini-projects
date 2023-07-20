from django.shortcuts import render
from register.models import Profile
from .models import *

def home(response):
    profile = Profile.objects.all()
    recipe = ImagesRecipesOwner.objects.all()
    return render(response, "home.html", {
        "profile":profile,
        "recipe": recipe
    })