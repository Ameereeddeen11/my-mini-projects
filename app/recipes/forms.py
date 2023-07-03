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
            "category",
        ]

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        exclude = ["name"]

class ImageForm(forms.ModelForm):
    pass

class FavoriteRecipeForm(forms.ModelForm):
    class Meta:
        model = FavoriteRecipe
        fields = [
            "user_id",
            "recipe_id",
        ]

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = [
            "user_id",
            "recipe_id",
            "score",
        ]