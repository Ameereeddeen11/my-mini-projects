from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegistertionForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]
    profile_pic = forms.ImageField(required=False)

class ProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(required=False)
    class Meta:
        model = Profile
        fields = [
            "profile_pic",
            "bio_user"
        ]

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [
            "username",
            "email"
        ]