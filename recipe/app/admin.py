from django.contrib import admin
from .models import *
from register.models import Profile

admin.site.register(Profile)
admin.site.register(ImagesRecipesOwner)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Recipes)