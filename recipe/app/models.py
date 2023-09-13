from django.db import models
from django.contrib.auth.models import User
from .validators import file_validators, validate_file_size, validate_int, validate_image_dimensions
from django.core.validators import FileExtensionValidator

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Recipes(models.Model):
    title = models.CharField(max_length=150)
    discription = models.TextField()
    ingredient = models.TextField(null=True)
    instructions = models.TextField()
    existing_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    own_category = models.CharField(max_length=150, null=True, blank=True)
    takes_time = models.CharField(max_length=80, null=True)
    for_how_many_people = models.IntegerField(null=True, validators=[validate_int])
    created_at = models.DateTimeField(auto_now_add=True)
    link_to_youtube = models.URLField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="image")
    likes = models.ManyToManyField(User, blank=False, related_name="likes")
    image = models.ImageField(upload_to='images/recipe/', default='unkown-profile.jpg', null=True, blank=True, 
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg']),
            file_validators,
            validate_file_size,
            validate_image_dimensions
        ]
    )

    def get_youtube_embed_url(self):
        youtube_id = self.link_to_youtube.split('/')[-1]
        embed_url = f'https://www.youtube.com/embed/{youtube_id}'
        return embed_url

    def __str__(self):
        return f"{self.title} - {self.discription} - {self.created_by} - {self.image}"

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    RATING_CHOICES = (
        (1, '1 - Moc nehutnalo'),
        (2, '2 - Jde to'),
        (3, '3 - Dobry'),
        (4, '4 - Hutnalo'),
        (5, '5 - Moc hutnalo')
    )

    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE, null=True)
    rating = models.PositiveIntegerField(choices=RATING_CHOICES, null=True, blank=True)

    def __str__(self):
        return f'{self.user_comment.username} - {self.comment} - {self.rating}'
