from django.shortcuts import render, redirect, get_object_or_404
from register.models import Profile
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

def home(request):
    profile = Profile.objects.all()
    recipe = ImagesRecipesOwner.objects.all()
    return render(request, "home.html", {
        "profile":profile,
        "images": recipe
    })

def search_recipe(request):
    if request.method == "GET":
        searched = request.GET["search"]
        post = Recipes.objects.filter(title__contains=searched)
        return render(request, "search_recipe.html", {
            "search": searched,
            "post": post,
        })
    else:
        return redirect("/recipe/")

@login_required()
def create(request):
    if request.method == "POST":
        image = request.FILES["image"]
        recipe = RecipeForm(request.POST)
        if recipe.is_valid():
            recipe.save()
            id_recipe = recipe.instance
            ImagesRecipesOwner.objects.create(
                recipe_id=id_recipe,
                image=image,
                created_by=request.user
            )
        return redirect("home")
    else:
        recipe = RecipeForm()
        image = ImageForm()
    return render(request, "create.html", {
        "form_recipe": recipe,
        "form_image": image
    })

def details(request, id):
    image = ImagesRecipesOwner.objects.get(id=id)
    recipe_id = image.recipe_id
    all_comment = Comment.objects.filter(recipe_id=recipe_id)
    if request.method == "POST":
        image = ImagesRecipesOwner.objects.get(id=id)
        recipe_id = image.recipe_id
        #comment = Comment.objects.create(
        #    user_comment=user_id,
        #    comment=comment_form,
        #    recipe_id=recipe_id
        #)
        #comment.save()
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.cleaned_data['comment']
            new_rating = comment_form.cleaned_data['rating']
            Comment.objects.create(
                user_comment=request.user,
                comment=new_comment,
                recipe_id=recipe_id,
                rating=new_rating
            )
    else:
        comment_form = CommentForm()
    return render(request, "detail.html", {
        "image": image,
        "comment_form": comment_form,
        "all_comment": all_comment
    })

@login_required()
def account_page(request):
    image = request.user.image.all()
    return render(request, "account.html", {"profile":image})

@login_required()
def edit(request, id):
    if request.user.image.all():
        recipe = Recipes.objects.get(id=id)
        image = ImagesRecipesOwner.objects.get(recipe_id=recipe)
        if request.method == "POST":
            recipe_form = RecipeForm(request.POST, instance=recipe)
            image_form = request.FILES.get("image") or None
            if recipe_form.is_valid():
                recipe_form.save()
                if image_form:
                    image.delete()
                    id_recipe = recipe_form.instance
                    ImagesRecipesOwner.objects.create(
                        recipe_id=id_recipe,
                        image=image_form,
                        created_by=request.user
                    )
                    return redirect("/recipe/account/")
        else:
            recipe = Recipes.objects.get(id=id)
            recipe_form = RecipeForm(instance=recipe)
            image = ImagesRecipesOwner.objects.get(recipe_id=recipe)
            image_form = ImageForm(instance=image)
        return render(request, "edit.html", {
            "recipe_form": recipe_form,
            "default_image": image,
            "image_form": image_form,
            "recipe": recipe
        })
    else:
        return render(request, "home.html")
@login_required()
def delete(request, id):
    delete_recipe = Recipes.objects.get(id=id)
    delete_image = ImagesRecipesOwner.objects.get(recipe_id=delete_recipe)
    if request.method == "POST":
        delete_recipe.delete()
        delete_image.delete()
        return redirect("/recipe/account/")
    return render(request, "delete.html", {
        "delete_recipe":delete_recipe,
        "delete_image":delete_image
    })

def profile(response, id):
    image = ImagesRecipesOwner.objects.filter(created_by=id)
    return render(response, "profile.html", {"images":image})

@login_required()
def likes(request, pk):
    recipe = get_object_or_404(ImagesRecipesOwner, id=pk)
    if recipe.likes.filter(id=request.user.id):
        recipe.likes.remove(request.user)
    else:
        recipe.likes.add(request.user)
    return redirect("home")