from django.shortcuts import render
from .form import RegistertionForm, ProfileForm, Profile
from recipes.models import ImagesRecipesOwner

def registretion(request):
    if request.method == "POST":
        form = RegistertionForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save(commit=False)

    else:
        form = RegistertionForm()
        profile_form = ProfileForm()
    return render(request, "register.html", {
        "form":form,
        "profile": profile_form
    })

def user_update(request, id):
    if request.method == "POST":
        profile_form = ProfileForm(request.FILES, request.POST)
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = ProfileForm()
    return render(request, "", {profile_form:"profile_form"})