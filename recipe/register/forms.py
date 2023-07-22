from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile 

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    profile_pic = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "profile_pic",
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "profile_pic",
            "bio_user",
        ]

class UpdateUser(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]