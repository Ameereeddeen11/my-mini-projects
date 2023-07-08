from django.contrib import admin
from .models import * 

admin.site.register(Category)
admin.site.register(Recipes)
admin.site.register(FavoriteRecipe)
admin.site.register(Rating)
admin.site.register(ImagesRecipes)
admin.site.register(RecipeOwner)