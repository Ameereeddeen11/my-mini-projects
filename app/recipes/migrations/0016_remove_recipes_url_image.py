# Generated by Django 4.2.1 on 2023-07-10 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_remove_recipes_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='url_image',
        ),
    ]
