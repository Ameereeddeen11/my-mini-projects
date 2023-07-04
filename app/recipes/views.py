from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages

def home(response):
    #recipe_pic = ImagesRecipes.objects.all()
    recipe = Recipes.objects.all()
    return render(response, "home.html", {
        #"recipes_pic":recipe_pic,
        "recipe":recipe
    })

def create(request):
    if request.method == "POST":
        form_recipe = RecipeForm()
        #form_image = ImageForm()
        #form_category = CategoryForm()
        if form_recipe.is_valid():
            fr = form_recipe.save(commit=False)
            fr.user = request.user
            fr.save()
        return redirect("home")
    else:
        form_recipe = RecipeForm()
        #form_image = ImageForm()
        #form_category = CategoryForm()
    return render(request, "create.html", {
        "form_recipe" : form_recipe,
        #"form_image" : form_image,
        #"form_category" : form_category
    })