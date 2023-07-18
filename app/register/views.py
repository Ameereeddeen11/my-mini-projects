from django.shortcuts import render
from .form import RegistertionForm, ProfileForm, Profile
from recipes.models import ImagesRecipesOwner
from django.contrib.auth import login

def registretion(request):
    if request.method == "POST":
        form = RegistertionForm(request.POST)
        #profile_form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            #profile_form.save(commit=False)
            profile_pic = form.cleaned_data.get("profile_pic")
            if profile_pic:
                user.profile.profile_pic = profile_pic
                user.profile.save()
            login(request, user)
    else:
        form = RegistertionForm()
        #profile_form = ProfileForm()
    return render(request, "register.html", {
        "form":form,
        #"profile": profile_form
    })

def user_update(request, id):
    if request.method == "POST":
        profile_form = ProfileForm(request.FILES, request.POST)
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = ProfileForm()
    return render(request, "", {profile_form:"profile_form"})