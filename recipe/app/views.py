from django.shortcuts import render, redirect, get_object_or_404
from register.models import Profile
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
import openai, json
from serpapi import GoogleSearch

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
        if post == None:    
            params = {
                "q": searched,
                "hl": "en",
                "gl": "us",
                "api_key": token["SERPAPI_KEY"],
            }
            search = GoogleSearch(params)
            result = search.get_dict()
            try:
                recipes_results = result["recipes_results"]
                ingredients_recipe = json.loads(json.dumps(recipes_results[0]["ingredients"]))
                return render(request, "search_recipe.html", {
                    "search": searched,
                    "post": post,
                    "result": recipes_results,
                    "ingredients": ingredients_recipe,
                })
            except:
                return render(request, "search_recipe.html", {
                    "search": searched,
                    "post": post
                })
        else:
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
        category = CategoryForm(request.POST)
        if recipe.is_valid() and not category.is_valid():
            recipe.save(commit=False)
            recipe.instance.created_by = request.user
            recipe.save()
        elif category.is_valid():
            category.save()
            recipe.save(commit=False)
            recipe.instance.created_by = request.user
            recipe.instance.existing_category = category.instance
            recipe.save()
    else:
        recipe = RecipeForm()
        category = CategoryForm()
    return render(request, "create.html", {
        "form_recipe": recipe,
        "category": category
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
            category = CategoryForm(request.POST, instance=recipe.existing_category)
            if recipe_form.is_valid() and not category.is_valid():
                recipe_form.save(commit=False)
                recipe_form.instance.created_by = request.user
                recipe_form.save()
            elif category.is_valid():
                category.save()
                recipe_form.save(commit=False)
                recipe_form.instance.created_by = request.user
                recipe_form.instance.existing_category = category.instance
                recipe_form.save()
        else:
            recipe = Recipes.objects.get(id=id)
            recipe_form = RecipeForm(instance=recipe)
            category = CategoryForm(instance=recipe.existing_category)
        return render(request, "edit.html", {
            "recipe_form": recipe_form,
            "recipe": recipe,
            "category": category
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
