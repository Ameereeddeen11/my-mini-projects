from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
import boto3

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
        #form_image = ImageForm()
        #form_category = CategoryForm()
        if form_recipe.is_valid():
            fr = form_recipe.save()
            # URL adress to AWS S3 images
            #s3_client = boto3.client('s3')
            #bucket_name = 'myminiprojectrecipe'
            #file_key = str(fr.image)
            #url = s3_client.generate_presigned_url('get_object', Params={'Bucket': bucket_name, 'Key': file_key}, ExpiresIn=3600)
            #fr.url_image = url
            fr.save()
            #RecipeOwner.objects.create(recipe_id=fr, created_by=request.user)
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