from django.shortcuts import render, redirect
from .forms import ProfileForm, RegisterForm, UpdateUser, Profile
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        profile = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile.is_valid():
            form.save()
            profile.save()
            redirect("login")
            #login(request, form.id)
        elif form.is_valid() and not profile.is_valid():
            form.save()
            profile_save = Profile.objects.create(user=form, profile="images/profile-pic/unkown-profile.jpg")
            profile_save.save()
    else:
        form = RegisterForm()
        profile = ProfileForm(request.POST, request.FILES)
    return render(request, "register.html", {
        "form":form,
        "profile": profile
    })

@login_required()
def account_setting(request):
    user = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=request.user.id)
    if request.method == "POST":
        update_info = UpdateUser(request.POST or None, instance=user)
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