from django.shortcuts import render
from .models import Profile
from .form import ProfileForm

def index(request):
    return render(request, "index.html", {})