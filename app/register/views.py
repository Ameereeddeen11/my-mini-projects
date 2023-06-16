from django.shortcuts import render
from .form import RegistertionForm

def registretion(response):
    if response.method == "POST":
        form = RegistertionForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegistertionForm()
    return render(response, "register.html", {"form":form})