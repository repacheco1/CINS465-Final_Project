from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    time = models.IntegerField()
    description = models.TextField(max_length=500)
    ingredients = models.TextField()
    optional_ingredients = models.TextField(blank=True)
    substitutions = models.TextField(blank=True)
    instructions = models.TextField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-created_on']

def unique_slug_generator(instance):
    constant_slug = slugify(instance.name)
    slug = constant_slug
    num = 0
    gen = instance.__class__
    while gen.objects.filter(slug=slug).exists():
        num += 1
        slug = "{slug}-{num}".format(slug=constant_slug, num=num)
    return slug

def pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug or instance.name != Recipe.objects.filter(slug=instance.slug):
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_reciever, sender=Recipe)
    

class Comment(models.Model):
    body = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    published_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_on']

    def __str__(self):
        return str(self.author) + " on " + str(self.recipe)

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