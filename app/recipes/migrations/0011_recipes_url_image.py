# Generated by Django 4.2.1 on 2023-07-04 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_recipes_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='url_image',
            field=models.URLField(null=True),
        ),
    ]