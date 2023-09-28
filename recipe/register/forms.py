from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile 
from app.validators import file_validators, validate_int, validate_file_size
from django.core.validators import FileExtensionValidator

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]

class ProfileForm(forms.ModelForm):
    profile_pic = forms.FileField(
        widget = forms.FileInput(
            attrs={
                'class':'form-control', 
                'accept':'.jpg, .png',
                'id': 'imageInput'
                }
        ),
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg']),
            file_validators,
            validate_file_size
        ]
    )
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