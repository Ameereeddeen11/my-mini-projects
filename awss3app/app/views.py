from django.shortcuts import render
from .models import Profile

def index(request):
    return render(request, "index.html", {})