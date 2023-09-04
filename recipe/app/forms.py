from django import forms 
from .models import *
from recipe.validators import ext_validator, file_validators, validate_int
from django.core.validators import FileExtensionValidator

class RecipeForm(forms.ModelForm):
    for_how_many_people = forms.IntegerField(validators=[validate_int])
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
            "link_to_youtube"
        ]
class CategoryForm(forms.ModelForm):
    name = forms.TextInput()
    class Meta:
        model = Category
        fields = ["name"]

class ImageForm(forms.ModelForm):
    image = forms.FileField(
        widget = forms.FileInput(attrs={'class':'form-control-file', 'accept':'.jpg, .png'}),
        validators=[]
    )
    required = False
    class Meta:
        model = ImagesRecipesOwner
        fields = [
            "image",
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "comment",
            "rating"
        ]