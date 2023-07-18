from django.shortcuts import render, redirect
from .form import RegistertionForm, ProfileForm, Profile
from recipes.models import ImagesRecipesOwner
from django.contrib.auth import login

def registretion(request):
    if request.method == "POST":
        form = RegistertionForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("/login/")
    else:
        form = RegistertionForm()
    return render(request, "register.html", {"form":form})

def user_update(request, id):
    if request.method == "POST":
        profile_form = ProfileForm(request.FILES, request.POST)
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = ProfileForm()
    return render(request, "", {profile_form:"profile_form"})