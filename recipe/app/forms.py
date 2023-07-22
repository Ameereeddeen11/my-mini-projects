from django import forms 
from .models import *

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = [
            "title",
            "discription",
            "ingredient",
            "instructions",
            "category"
        ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.FileInput(attrs={'class':'form-control-file'})
    )
    class Meta:
        model = ImagesRecipesOwner
        exclude = ["image"]

class FavoriteRecipeForm(forms.ModelForm):
    class Meta:
        model = FavoriteRecipe
        fields = [
            "recipe_id",
        ]

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = [
            "recipe_id",
            "score",
        ]