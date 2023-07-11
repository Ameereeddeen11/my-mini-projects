from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages


def home(response):
    recipe = Recipes.objects.all()
    image = ImagesRecipesOwner.objects.all()
    
    return render(response, "home.html", {
        "images":image,
        "recipe":recipe
    })

def create(request):
    if request.method == "POST" and request.FILES.get('image'):
        form_recipe = RecipeForm(request.POST, request.FILES)
        form_image = request.FILES["image"]
        #form_category = CategoryForm()
        if form_recipe.is_valid():
            fr = form_recipe.save()
            fr.save()
            ImagesRecipesOwner.objects.create(
                recipe_id=fr, 
                image= form_image, 
                created_by=request.user
            )
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

def detail(response, id):
    image = ImagesRecipesOwner.objects.get(id=id)
    return render(response, "detail.html", {"image":image})