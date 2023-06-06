from django.contrib import admin
from .models import * 

admin.site.register(Category)
admin.site.register(Recipes)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(FavoriteRecipe)
admin.site.register(Rating)