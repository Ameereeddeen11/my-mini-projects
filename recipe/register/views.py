from django.shortcuts import render, redirect
from .forms import RegisterForm, UpdateUser, Profile, ProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            if not profile.profile_pic:
                profile.profile_pic = "images/profile-pic/unkown-profile.jpg"
                profile.save()
            redirect("/login/")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form":form})

@login_required()
def account_setting(request):
    user = request.user
    profile = user.profile
    if request.method == "POST":
        update_info = UpdateUser(request.POST, instance=user)
        update_profile = ProfileForm(request.POST, request.FILES, instance=profile)
        if update_info.is_valid() and update_profile.is_valid():
            update_info.save()
            update_profile.save()
    else:
        update_info = UpdateUser(request.POST, instance=user)
        update_profile = ProfileForm(request.POST, request.FILES, instance=profile)
    return render(request, "update-user.html", {
        "form_profile": update_profile,
        "form_updateuser": update_info
    })