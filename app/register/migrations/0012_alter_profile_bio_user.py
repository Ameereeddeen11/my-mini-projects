# Generated by Django 4.2.1 on 2023-07-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_alter_profile_bio_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio_user',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
