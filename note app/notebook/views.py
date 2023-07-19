from django.shortcuts import render, redirect
from notebook.forms import ItemForm
from .models import *

def home(response):
    item = Item.objects.all()
    return render(response, "home.html", {
        "item":item   
    })

def create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect("/note/")
    else:
        form = ItemForm()
        item = Item.objects.all()
    return render(request, "create.html", {
        "form":form,
        "item":item,    
    })

def detail(request, id):
    item = Item.objects.all()
    card = Item.objects.get(id=id)  
    return render(request, "detail.html", {
        "card":card,
        "item":item,
    })