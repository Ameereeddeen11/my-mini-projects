from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Recipes(models.Model):
    title = models.CharField(max_length=150)
    discription = models.TextField()
    ingredient = models.TextField(null=True)
    instructions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "f{self.title} - {self.discription}"


class ImagesRecipesOwner(models.Model):
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to='images/recipe/', default='unkown-profile.jpg', null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.created_by


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
        return f'{self.user_id.username} - {self.recipe_id.title({self.score})}'
