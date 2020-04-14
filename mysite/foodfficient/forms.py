
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from foodfficient.models import Profile
from django.forms import modelformset_factory, formset_factory
from django.db import models
from .models import (Recipe, RequiredIngredients, OptionalIngredients, Substitutions, Instructions)

def must_be_unique(value):
    user = User.objects.filter(email=value)
    if len(user) > 0:
        raise forms.ValidationError("Email Already Exists")
    # Always return the cleaned data, whether you have changed it or
    # not.
    return value

class RecipeModelForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'recipe_picture', 'recipe_time',)
        labels = {
            'recipe_name': 'Recipe name:',
            'recipe_picture': 'Recipe picture:', 
            'recipe_time': 'Recipe cooking time (minutes):',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter recipe name here'
                }
            ),
            'name': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose recipe image...'
                }
            ),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter cooking time here:'
                }
            ),
        }

RequiredIngredientsFormset = modelformset_factory(
    RequiredIngredients,
    fields=('required_ingredient', ),
    extra=1,
    widgets={
        'required_ingredient': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter required ingredient here:'
            }
        )
    }
)

OptionalIngredientsFormset = modelformset_factory(
    OptionalIngredients,
    fields=('optional_ingredient', ),
    extra=1,
    widgets={
        'optional_ingredient': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter optional ingredient here:'
            }
        )
    }
)

SubstitutionsFormset = modelformset_factory(
    Substitutions,
    fields=('substitutions', ),
    extra=1,
    widgets={
        'substitutions': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter substitution here:'
            }
        )
    }
)

InstructionsFormset = modelformset_factory(
    Instructions,
    fields=('required_instructions', 'optional_instructions', 'substitution_instructions', ),
    extra=1,
    widgets={
        'required_instructions': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter required instructions here:'
            }
        ),
        'optional_instructions': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter optional instructions here:'
            }
        ),
        'substitution_instructions': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter substitution instructions here:'
            }
        ),
    }
)




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