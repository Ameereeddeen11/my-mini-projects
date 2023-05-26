from django.shortcuts import render
from . import models

def home(response):
    return render(response, "home.html", {})