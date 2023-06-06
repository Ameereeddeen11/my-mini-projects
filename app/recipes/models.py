from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Recipes(models.Model):
    title = models.CharField(max_length=150)
    discription = models.TextField()
    ingredient = models.ManyToManyField('Ingredient', through='RecipeIngredient')
    instructions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "f{self.title} - {self.discription} - {self.created_by.username}"
    
class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.ingredient.name} ({self.quantity})'
    
class FavoriteRecipe(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_id.username} - {self.recipe.title}"
    
class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.user_id.username} - {self.recipe_id.title ({self.score})}'
