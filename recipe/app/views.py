from django.shortcuts import render, redirect
from register.models import Profile
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

def home(response):
    profile = Profile.objects.all()
    recipe = ImagesRecipesOwner.objects.all()
    return render(response, "home.html", {
        "profile":profile,
        "recipe": recipe
    })

@login_required()
def create(request):
    if request.method == "POST":
        image = request.FILES["image"]
        recipe = RecipeForm(request.POST)
        if recipe.is_valid():
            recipe.save()
            ImagesRecipesOwner.objects.create(
                recipe_id = recipe,
                image = image,
                create_by = request.user
            )
        return redirect("home")
    else:
        recipe = RecipeForm()
        image = ImageForm()
    return render(request, "create.html", {
        "form_recipe": recipe,
        "form_image": image
    })

@login_required()
def edit(request, id):
    recipe = Recipes.objects.get(id=id)
    image = ImagesRecipesOwner.objects.get(recipe_id=id)
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, instance=recipe)
        image_form = ImageForm(request.FILES, instance=image)
        if recipe_form.is_valid() and image_form.is_valid():
            recipe_form.save()
            image_form.save()
            return redirect("/home/")
    else:
        recipe = Recipes.objects.get(id=id)
        recipe_form = RecipeForm(instance=recipe)
        image = ImagesRecipesOwner.objects.get(recipe_id=id)
        image_form = ImageForm(instance=image)
    return render(request, "edit.html", {
        "recipe_form": recipe_form,
        "image": image,
        "image_form": image_form
    })