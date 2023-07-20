from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form)
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form":form})

