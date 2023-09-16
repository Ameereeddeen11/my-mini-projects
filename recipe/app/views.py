from django.shortcuts import render, redirect, get_object_or_404
from register.models import Profile
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
import openai, json

file_path = open('data/aws_s3.json', 'r')
token = json.load(file_path)

def home(request):
    profile = Profile.objects.all()
    recipe = Recipes.objects.all()
    return render(request, "home.html", {
        "profile":profile,
        "images":recipe
    })

def search_recipe(request):
    if request.method == "GET":
        searched = request.GET["search"]
        post = Recipes.objects.filter(title__contains=searched).all()
        return render(request, "search_recipe.html", {
            "search": searched,
            "post": post
        })
    else:
        return redirect("/recipe/")

@csrf_protect
@login_required()
def create(request):
    if request.method == "POST":
        recipe = RecipeForm(request.POST, request.FILES)
        if recipe.is_valid():
            recipe.save(commit=False)
            recipe.instance.created_by = request.user
            recipe.save()
    else:
        recipe = RecipeForm()
    return render(request, "create.html", {
        "form_recipe": recipe
    })

openai.api_key = token["OPENAI_API_KEY"]

def recipes_by_ai(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        promt = ("Recipe by this ingredients: " + user_input)
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = promt,
            max_tokens = 150,
            n = 1,
            stop = None,
            temperature = 0.7
        )
        ai_response = response.choices[0].text.strip()
        return render(request, "openai.html", {"response":ai_response})
    return render(request, "openai.html", {})

def details(request, id):
    image = Recipes.objects.get(id=id)
    profile = Profile.objects.get(user=image.created_by.id)
    all_comment = Comment.objects.filter(recipe_id=image)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.cleaned_data['comment']
            new_rating = comment_form.cleaned_data['rating']
            Comment.objects.create(
                user_comment=request.user,
                comment=new_comment,
                recipe_id=image,
                rating=new_rating
            )
    else:
        comment_form = CommentForm()
    return render(request, "details.html", {
        "image": image,
        "comment_form": comment_form,
        "all_comment": all_comment,
        "profile": profile
    })

@login_required()
def account_page(request):
    image = request.user.image.all()
    return render(request, "account.html", {"profile":image})

@login_required()
def likes_page(request):
    image = request.user.likes.all()
    return render(request, "likes.html", {"profile":image})

@csrf_protect
@login_required()
def edit(request, id):
    if request.user.image.all():
        recipe = Recipes.objects.get(id=id)
        if request.method == "POST":
            recipe_form = RecipeForm(request.POST, request.FILES, instance=recipe)
            if recipe_form.is_valid():
                recipe_form.save()
        else:
            recipe = Recipes.objects.get(id=id)
            recipe_form = RecipeForm(instance=recipe)
        return render(request, "edit.html", {
            "recipe_form": recipe_form,
            "recipe": recipe
        })
    else:
        return render(request, "home.html")
    
@login_required()
def delete(request, id):
    delete_recipe = Recipes.objects.get(id=id)
    if request.method == "POST":
        delete_recipe.delete()
        return redirect("/account/")
    return render(request, "delete.html", {
        "delete_recipe":delete_recipe
    })

def profile(response, id):
    image = Recipes.objects.filter(created_by=id)
    return render(response, "profile.html", {"images":image})

@login_required()
def likes(request, pk):
    recipe = get_object_or_404(Recipes, id=pk)
    if recipe.likes.filter(id=request.user.id):
        recipe.likes.remove(request.user)
    else:
        recipe.likes.add(request.user)
    return redirect("home")
