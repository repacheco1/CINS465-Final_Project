# Generated by Django 3.0.4 on 2020-04-18 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import foodfficient.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('prep_time', models.IntegerField()),
                ('cook_time', models.IntegerField()),
                ('total_time', models.IntegerField()),
                ('image', models.ImageField(blank=True, max_length=500, null=True, upload_to=foodfficient.models.upload_to_recipies)),
                ('description', models.TextField(max_length=500)),
                ('ingredients', models.TextField()),
                ('optional_ingredients', models.TextField(blank=True)),
                ('substitutions', models.TextField(blank=True)),
                ('instructions', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=35)),
                ('avatar', models.ImageField(blank=True, max_length=500, null=True, upload_to=foodfficient.models.upload_to_avatars)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=500)),
                ('published_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='foodfficient.Recipe')),
            ],
            options={
                'ordering': ['-published_on'],
            },
        ),
    ]
