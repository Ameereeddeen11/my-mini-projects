from django.shortcuts import render, redirect
from .models import *

def home(response):
    item = Item.objects.all()
    return render(response, "home.html", {
        "item":item   
    })

def create(request):
    return render(request, "create.html", {})