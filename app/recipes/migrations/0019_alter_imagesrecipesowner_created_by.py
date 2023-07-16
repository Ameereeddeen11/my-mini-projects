# Generated by Django 4.2.1 on 2023-07-16 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0018_alter_imagesrecipesowner_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesrecipesowner',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
