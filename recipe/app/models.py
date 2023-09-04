from django.db import models
from django.contrib.auth.models import User
#from recipe.validators import file_validators, ext_validator, validate_image_dimensions, validate_int
from file_validator.models import DjangoFileValidator
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import magic

ext_validator = FileExtensionValidator(['png', 'jpg'])

def file_validators(value):
    accept = ['image/png', 'image/jpeg']
    file_type = magic.from_buffer(value.read(1024), mime=True)
    print(file_type)
    if file_type not in accept:
        raise ValidationError("Unsupported file type")
        
#def validate_image_dimensions(value):
#    max_width = 800
#    max_height = 600
#
#    image = Image.open(value)
#    width, height = image.size
#    if width > max_width or height > max_height:
#        raise ValidationError(f"Obrázek má příliš velké rozměry. Maximální rozměry jsou {max_width}x{max_height} px.")

def validate_int(value):
    if value <= 0:
        raise ValidationError(
            ("The reacipe must be for more than %(value) people"),
            params={"value": value},
        )

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

    def get_youtube_embed_url(self):
        youtube_id = self.link_to_youtube.split('/')[-1]
        embed_url = f'https://www.youtube.com/embed/{youtube_id}'
        return embed_url

    def __str__(self):
        return f"{self.title} - {self.discription}"


class ImagesRecipesOwner(models.Model):
    recipe_id = models.ForeignKey(Recipes, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/recipe/', default='unkown-profile.jpg', null=True, blank=True, validators=[file_validators])
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="image")
    likes = models.ManyToManyField(User, blank=False, related_name="likes")

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.created_by} - {self.image}"


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
