from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views import generic
from django.db import transaction
from . import forms, models
# from models import Recipe, RequiredIngredients, OptionalIngredients, Substitutions, Instructions
from .forms import (
    RecipeModelForm,
    RequiredIngredientsFormset,
    OptionalIngredientsFormset,
    SubstitutionsFormset,
    InstructionsFormset
)
from .models import (
    Recipe,
    RequiredIngredients,
    OptionalIngredients,
    Substitutions,
    Instructions
)

def logoutPageView(request):
    logout(request)
    return redirect("/")

def homePageView(request):
    indexContext = {
        "title":"Home - Foodfficient",
        "pageTitle":"Welcome to Foodfficient!",
        "body":"",
        "body2":"",
    }
    return render(request, "index.html", context=indexContext)

def profilePageView(request):
    if request.method == "POST":
        form_instance = forms.ProfileForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/profile/")
            # print("Hi")
    else:
        form_instance = forms.ProfileForm
    profileContext = {
        "title":"Profile - Foodfficient",
        "pageTitle":"Welcome to profiles Foodfficient!",
        "body":"",
        "body2":"",
    }
    return render(request, "profile.html", context=profileContext)
# Create your views here.

def registerPageView(request):
    if request.method == "POST":
        form_instance = forms.RegistrationForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("/login/")
            # print("Hi")
    else:
        form_instance = forms.RegistrationForm()
    registerContext = {
        "title":"Registration - Foodfficient",
        "pageTitle":"Welcome to Foodfficient! Start by creating an account.",
        "form":form_instance,
    }
    return render(request, "registration/register.html", context=registerContext)

def aboutPageView(request):
    aboutContext = {
        "title":"About - Foodfficient",
        "pageTitle":"Welcome to about Foodfficient!",
        "body":"",
        "body2":"",
    }
    return render(request, "about.html", context=aboutContext)

class RecipeListView(generic.ListView):
    model: Recipe
    context_object_name = 'recipe'
    template_name="recipe.html"

@login_required

def addRecipePageView(request):
    if request.method == 'GET':
        recipeForm = RecipeModelForm(request.GET or None)
        requiredForm = RequiredIngredientsFormset(queryset=RequiredIngredients.objects.none())
        optionalForm = OptionalIngredientsFormset(queryset=OptionalIngredients.objects.none())
        substitutionsForm = SubstitutionsFormset(queryset=Substitutions.objects.none())
        instructionsForm = InstructionsFormset(queryset=Instructions.objects.none())
    elif request.method == 'POST':
        recipeForm = RecipeModelForm(request.POST)
        requiredForm = RequiredIngredientsFormset(request.POST)
        optionalForm = OptionalIngredientsFormset(request.POST)
        substitutionsForm = SubstitutionsFormset(request.POST)
        instructionsForm = InstructionsFormset(request.POST)
    if recipeForm.is_valid() and requiredForm.is_valid() and optionalForm.is_valid() and substitutionsForm.is_valid() and instructionsForm.is_valid():
        recipe = recipeForm.save()
        for form in requiredForm:
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
        for form in optionalForm:
            optional = form.save(commit=False)
            optional.recipe = recipe
            optional.save()
        for form in substitutionsForm:
            subs = form.save(commit=False)
            subs.recipe = recipe
            subs.save()
        for form in instructionsForm:
            ins = form.save(commit=False)
            ins.recipe = recipe
            ins.save()
        return redirect('Recipes')
    addContext = {
        'recipe': recipeForm,
        'requiredForm': requiredForm,
        'optional': optionalForm,
        'substitutios': substitutionsForm,
        'instructions': instructionsForm,
        "title":"Add Recipe - Foodfficient",
        "pageTitle":"Welcome to add a recipe Foodfficient!",
        "body":"",
        "body2":"",
    }
    return render(request, "addRecipe.html", context=addContext)


# @transaction.atomic
# def profilePageView(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('/profile/')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     profileContext = {
#         "title":"Profile - Foodfficient",
#         "pageTitle":"Welcome to profiles Foodfficient!",
#         "body":"",
#         "body2":"",
#     }
#     return render(request, "profile.html", {
#         'user_form': user_form,
#         'profile_form': profile_form
#     }, context=profileContext)