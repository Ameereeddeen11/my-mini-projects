# Generated by Django 4.2.1 on 2023-07-10 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0014_imagesrecipesowner_remove_recipeowner_created_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='image',
        ),
    ]