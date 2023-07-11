from django.shortcuts import render
from .form import RegistertionForm, ProfileForm

def registretion(response):
    if response.method == "POST":
        form = RegistertionForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegistertionForm()
    return render(response, "register.html", {"form":form})

def user_update(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.FILES, request.POST)
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = ProfileForm()
    return render(request, "", {profile_form:"profile_form"})