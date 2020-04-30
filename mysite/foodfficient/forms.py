
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from foodfficient.models import Profile
from django.forms import modelformset_factory, formset_factory
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from django.db import models
from . import models
from .models import Comment, Recipe, Blog
from .recipe_utils import CUISINE_CHOICES, DIET_CHOICES

def must_be_unique(value):
    user = User.objects.filter(email=value)
    if len(user) > 0:
        raise forms.ValidationError("Email Already Exists")
    return value


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        validators=[must_be_unique]
        )

    class Meta:
        model = User
        fields = ("username", "first_name", "email", 
                  "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'avatar', 'facebook', 'instagram', 'pinterest')


class RecipeForm(forms.Form):
    name = forms.CharField(label='Name: ', max_length=50)
    prep_time = forms.IntegerField(label='Prep Time (minutes): ', min_value=0)
    cook_time = forms.IntegerField(label='Cook Time (minutes): ', min_value=0)
    servings = forms.IntegerField(label='Servings: ', min_value=0)
    cuisine = forms.ChoiceField(choices=CUISINE_CHOICES)
    diet = forms.MultipleChoiceField(choices=DIET_CHOICES, required=False, widget=forms.CheckboxSelectMultiple)
    image = forms.ImageField(label='Submit picture: ', max_length=500)
    description = forms.CharField(label='Description: ', max_length=500, widget=forms.Textarea)
    ingredients = forms.CharField(label='Ingredients: ', widget=forms.Textarea)
    instructions = forms.CharField(label='Instructions: ', widget=forms.Textarea)
    notes = forms.CharField(label='Notes: ', widget=forms.Textarea, required=False)

    def save(self, request):
        recipe_instance = models.Recipe()
        recipe_instance.name = self.cleaned_data["name"]
        recipe_instance.prep_time = self.cleaned_data["prep_time"]
        recipe_instance.cook_time = self.cleaned_data["cook_time"]
        recipe_instance.servings = self.cleaned_data["servings"]
        recipe_instance.cuisine = self.cleaned_data["cuisine"]
        recipe_instance.diet = self.cleaned_data["diet"]
        recipe_instance.image = self.cleaned_data["image"]
        recipe_instance.description = self.cleaned_data["description"]
        recipe_instance.ingredients = self.cleaned_data["ingredients"]
        recipe_instance.instructions = self.cleaned_data["instructions"]
        recipe_instance.notes = self.cleaned_data["notes"]
        recipe_instance.author = request.user
        recipe_instance.total_time = self.cleaned_data["prep_time"] + self.cleaned_data["cook_time"]
        recipe_instance.save()
        
        return recipe_instance

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content')
    content = SummernoteTextFormField()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        labels = {'body': 'Comment: '}
        fields = ('body', )