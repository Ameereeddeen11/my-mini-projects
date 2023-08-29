from django.shortcuts import render, redirect
from .forms import ProfileForm, RegisterForm, Profile, UpdateUser
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            profile_pic = form.cleaned_data("profile_pic")
            user = form.save()
            profile = Profile.objects.create(user=user, profile_pic=profile_pic)
            if not profile.profile_pic:
                profile.profile_pic = "images/profile-pic/unkown-profile.jpg"
                profile.save()
            # login
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user_authenticate = authenticate(username=username, password=password1)
            login(request, user_authenticate)
            return redirect('/') 
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form":form})

@csrf_protect
@login_required()
def account_settings(request):
    user = request.user
    profile = request.user.profile
    if request.method == "POST":
        update_info = UpdateUser(request.POST, instance=user)
        update_profile = ProfileForm(request.POST, request.FILES, instance=profile)
        if update_info.is_valid() and update_profile.is_valid():
            update_info.save()
            update_profile.save()
    else:
        update_info = UpdateUser(instance=user)
        update_profile = ProfileForm(instance=profile)
    return render(request, "update-user.html", {
        "form_profile": update_profile,
        "form_updateuser": update_info
    })