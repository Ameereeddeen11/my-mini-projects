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

