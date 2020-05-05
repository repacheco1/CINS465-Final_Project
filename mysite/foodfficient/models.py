from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.text import slugify
from .recipe_utils import CUISINE_CHOICES, DIET_CHOICES
from multiselectfield import MultiSelectField

#Change name avatar picture
def upload_to_avatars(instance, filename):
    ext = filename.split('.')[-1]
    return 'avatars/%s/%s.%s' % (instance.user.username, instance.user.username, ext)

#Change name recipe picture
def upload_to_recipies(instance, filename):
    ext = filename.split('.')[-1]
    return 'recipies/%s/%s.%s' % (instance.author.username, instance.slug, ext)

#Recipe Model
class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    total_time = models.IntegerField()
    servings = models.IntegerField()
    cuisine = models.IntegerField(choices=CUISINE_CHOICES)
    diet = MultiSelectField(choices=DIET_CHOICES)
    image = models.ImageField(
        max_length=500,
        upload_to=upload_to_recipies,
        null=True,
        blank=True)
    description = models.TextField()
    ingredients = models.TextField()
    notes = models.TextField(blank=True)
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

# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # slug = models.SlugField(max_length=200, unique=True)
    avatar = models.ImageField(
        max_length=500,
        upload_to=upload_to_avatars,
        null=True,
        blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=35, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    pinterest = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Blog Model
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    published_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_on']

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

def unique_slug_generator_blog(instance):
    constant_slug = slugify(instance.title)
    slug = constant_slug
    num = 0
    gen = instance.__class__
    while gen.objects.filter(slug=slug).exists():
        num += 1
        slug = "{slug}-{num}".format(slug=constant_slug, num=num)
    return slug

def pre_save_reciever_blog(sender, instance, *args, **kwargs):
    if not instance.slug or instance.title != Blog.objects.filter(slug=instance.slug):
        instance.slug = unique_slug_generator_blog(instance)

pre_save.connect(pre_save_reciever_blog, sender=Blog)

# Comment model
class Comment(models.Model):
    body = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    entry = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', null=True)
    published_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_on']

    def __str__(self):
        return str(self.author) + " on " + str(self.entry)