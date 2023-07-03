from django.shortcuts import render
from .models import *
from .forms import *

def home(response):
    recipe_pic = ImagesRecipes.objects.all()
    return render(response, "home.html", {"recipes_pic":recipe_pic})

def create(request):
    form_recipe = RecipeForm()
    form_ingredient = IngredientForm()
    return render(request, "create.html", {
        "form_recipe" : form_recipe,
        "form_ingredient" : form_ingredient
    })