from django.shortcuts import render
from register.models import Profile

def home(response):
    profile = Profile.objects.all()
    return render(response, "home.html", {"profile":profile})