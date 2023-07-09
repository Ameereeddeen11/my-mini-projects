from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
import boto3
import hashlib

def home(response):
    #recipe_pic = ImagesRecipes.objects.all()
    recipe = Recipes.objects.all()
    return render(response, "home.html", {
        #"recipes_pic":recipe_pic,
        "recipe":recipe
    })

def create(request):
    if request.method == "POST":
        form_recipe = RecipeForm(request.POST, request.FILES)
        form_image = request.FILES.getlist("image")
        #form_category = CategoryForm()
        if form_recipe.is_valid():
            fr = form_recipe.save()
            fr.save()
            for img in form_image:
                #hash_sha256_value = hashlib.sha256(img.encode('utf-8')).hexdigest()
                ImagesRecipesOwner.objects.create(recipe_id=fr, image=img, created_by=request.user)
        return redirect("home")
    else:
        form_recipe = RecipeForm()
        form_image = ImageForm()
        #form_category = CategoryForm()
    return render(request, "create.html", {
        "form_recipe" : form_recipe,
        "form_image" : form_image,
        #"form_category" : form_category
    })