from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_picture = models.ImageField(upload_to='images/', blank=True)
    recipe_time = models.IntegerField(blank=True)

    class Meta:
        db_table = 'recipe'

    def __str__(self):
        return self.name

    def get_requiredIngredients(self):
        return ', '.join(self.required_ingredients.all().values_list('required_ingredients', flat=True))

    def get_optionalIngredients(self):
        return ', '.join(self.optional_ingredients.all().values_list('optional_ingredients', flat=True))

    def get_substitutions(self):
        return ', '.join(self.substitutions.all().values_list('substitutions', flat=True))

    def get_instructions(self):
        return ', '.join(self.instructions.all().values_list('instructions', flat=True))


class RequiredIngredients(models.Model):
    required_ingredient = models.CharField(max_length=75)
    recipe_name = models.ForeignKey(
        Recipe,
        related_name='required_ingredients',
        on_delete=models.SET_NULL,
        null=True)

    class Meta:
        db_table = 'required_ingredients'

    def __str__(self):
        return self.name

class OptionalIngredients(models.Model):
    optional_ingredient = models.CharField(max_length=75)
    recipe_name = models.ForeignKey(
        Recipe,
        related_name='optional_ingredients',
        on_delete=models.SET_NULL,
        null=True)

    class Meta:
        db_table = 'optional_ingredients'

    def __str__(self):
        return self.name

class Substitutions(models.Model):
    substitutions = models.CharField(max_length=75)
    recipe_name = models.ForeignKey(
        Recipe,
        related_name='substitutions',
        on_delete=models.SET_NULL,
        null=True)

    class Meta:
        db_table = 'substitutions'

    def __str__(self):
        return self.name

class Instructions(models.Model):
    required_instructions = models.TextField(max_length=500)
    optional_instructions = models.TextField(max_length=500)
    substitution_instructions = models.TextField(max_length=500)
    recipe_name = models.ForeignKey(
        Recipe,
        related_name='instructions',
        on_delete=models.SET_NULL,
        null=True)

    class Meta:
        db_table = 'instructions'

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=35, blank=True)
    avatar = models.ImageField(upload_to='images/', blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
