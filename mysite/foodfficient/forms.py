
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from foodfficient.models import Profile
from django.forms import modelformset_factory, formset_factory
from django.db import models
from . import models
from .models import Comment

def must_be_unique(value):
    user = User.objects.filter(email=value)
    if len(user) > 0:
        raise forms.ValidationError("Email Already Exists")
    # Always return the cleaned data, whether you have changed it or
    # not.
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
        fields = ('bio', 'location', 'avatar')


class RecipeForm(forms.Form):
    name = forms.CharField(label='Name: ', max_length=50)
    time = forms.IntegerField(label='Total Time (minutes): ', min_value=0)
    description = forms.CharField(label='Description: ', max_length=500, widget=forms.Textarea)
    ingredients = forms.CharField(label='Ingredients: ', widget=forms.Textarea)
    optional_ingredients = forms.CharField(label='Optional Ingredients: ',widget=forms.Textarea, required=False)
    substitutions = forms.CharField(label='Substitutions: ', widget=forms.Textarea, required=False)
    instructions = forms.CharField(label='Instructions: ', widget=forms.Textarea)

    def save(self, request):
        recipe_instance = models.Recipe()
        recipe_instance.name = self.cleaned_data["name"]
        recipe_instance.time = self.cleaned_data["time"]
        recipe_instance.description = self.cleaned_data["description"]
        recipe_instance.ingredients = self.cleaned_data["ingredients"]
        recipe_instance.optional_ingredients = self.cleaned_data["optional_ingredients"]
        recipe_instance.substitutions = self.cleaned_data["substitutions"]
        recipe_instance.instructions = self.cleaned_data["instructions"]
        recipe_instance.author = request.user
        recipe_instance.save()
        return recipe_instance

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        labels = {'body': 'Comment: '}
        fields = ('body', )
