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
    image = forms.ImageField(
        widget=forms.FileInput(attrs={'class':'form-control-file'})
    )
    required = False
    class Meta:
        model = ImagesRecipesOwner
        fields = ["image",]

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]