from django import forms 
from .models import *
from .validators import file_validators, validate_int, validate_file_size
from django.core.validators import FileExtensionValidator

class RecipeForm(forms.ModelForm):
    for_how_many_people = forms.IntegerField(validators=[validate_int])
    image = forms.FileField(
        widget = forms.FileInput(attrs={'class':'form-control', 'accept':'.jpg, .png'}),
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg']),
            file_validators,
            validate_file_size
        ]
    )
    class Meta:
        model = Recipes
        fields = [
            "title",
            "discription",
            "ingredient",
            "instructions",
            "existing_category",
            "own_category",
            "takes_time",
            "for_how_many_people",
            "link_to_youtube",
            "image"
        ]

class CategoryForm(forms.ModelForm):
    name = forms.TextInput()
    class Meta:
        model = Category
        fields = ["name"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "comment",
            "rating"
        ]