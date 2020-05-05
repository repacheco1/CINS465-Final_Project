# Generated by Django 3.0.6 on 2020-05-05 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodfficient', '0003_auto_20200504_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
