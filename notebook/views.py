from django.shortcuts import render, redirect
from .models import *

def home(response):
    return render(response, "home.html", {})

def create(request):
    return render(request, "create.html", {})