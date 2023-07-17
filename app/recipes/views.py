from django.shortcuts import render, redirect
#from .models import *
from .forms import *
#from django.contrib import messages
from register.models import Profile
from register.form import ProfileForm, UpdateUserForm
from django.contrib.auth.decorators import login_required


def home(response):
    image = ImagesRecipesOwner.objects.all()
    profile = Profile.objects.all()
    return render(response, "home.html", {
        "images": image,
        "profile": profile
    })

@login_required()
def create(request):
    if request.method == "POST" and request.FILES.get('image'):
        form_recipe = RecipeForm(request.POST, request.FILES)
        form_image = request.FILES["image"]
        # form_category = CategoryForm()
        if form_recipe.is_valid():
            fr = form_recipe.save()
            fr.save()
            ImagesRecipesOwner.objects.create(
                recipe_id=fr,
                image=form_image,
                created_by=request.user
            )
        return redirect("home")
    else:
        form_recipe = RecipeForm()
        form_image = ImageForm()
        # form_category = CategoryForm()
    return render(request, "create.html", {
        "form_recipe": form_recipe,
        "form_image": form_image,
        # "form_category" : form_category
    })


def detail(response, id):
    image = ImagesRecipesOwner.objects.get(id=id)
    return render(response, "detail.html", {"image": image})

@login_required()
def account_settings(request):
    if request.method == "POST":
        form_updateuser = UpdateUserForm(request.POST, instance=request.user)
        form_profile = ProfileForm(request.FILES, request.POST, instance=request.user.profile)
        if form_profile.is_valid() and form_updateuser.is_valid():
            form_profile.save()
            form_updateuser.save()
            return redirect("/account-settings/")
    else:
        form_updateuser = UpdateUserForm(instance=request.user)
        form_profile = ProfileForm(instance=request.user.profile)
    return render(request, "account-settings.html", {
        "form_profile": form_profile,
        "form_updateuser": form_updateuser
    })
@login_required()
def account(request):
    image = request.user.imagesrecipesowner_set.all()
    if request.method == "POST":
        return redirect("/account/")
    return render(request, "account.html", {"profile": image})

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

def delete(request, id):
    delete_recipe = Recipes.objects.get(id=id)
    delete_image = ImagesRecipesOwner.objects.get(recipe_id=id)
    if request.method == "POST":
        delete_recipe.delete()
        delete_image.delete()
        return redirect("/account/")
    return render(request, "delete.html", {
        "delete_recipe": delete_recipe,
        "delete_image": delete_image
    })


