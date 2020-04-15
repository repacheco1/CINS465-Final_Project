from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Recipe(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    name = models.CharField(max_length=50)
    time = models.IntegerField()
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Comment(models.Model):
    body = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author) + ": " + self.body

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=35, blank=True)
    avatar = models.ImageField(
        max_length=144,
        upload_to='avatars',
        null=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

    # uploads/%Y/%m/%d/