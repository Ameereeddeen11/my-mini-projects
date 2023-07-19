from django.shortcuts import render
from .forms import Registrations

def register(request):
    if request.method == "POST":
        form = Registrations(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Registrations()
    return render(request, "registrations.html", {"form":form})