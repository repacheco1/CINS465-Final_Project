from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from . import models, forms

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
    # if request.method == "POST":
    #     form_instance = forms.ProfileForm(request.POST)
    #     if form_instance.is_valid():
    #         form_instance.save()
    #         return redirect("/profile/")
    #         # print("Hi")
    # else:
    #     form_instance = forms.ProfileForm
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

def recipePageView(request):
    form = forms.RecipeForm()
    recipe_list = models.RecipeModels.objects.all()
    aboutContext = {
        "title":"Recipes - Foodfficient",
        "pageTitle":"Here is a list of all recipes on Foodfficient!",
        "body":"",
        "body2":"",
        "table0":"Recipe Title",
        "table1":"Recipe Time",
        "table2":"Recipe Description",
        "table3":"Recipe Ingredients",
        "table4":"Recipe Instructions",
        "recipe_list":recipe_list,
        "form":form,
    }
    return render(request, "recipes.html", context=aboutContext)


@login_required

def addRecipePageView(request):
    if request.method == "POST":
        form = forms.RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            form = forms.RecipeForm()
            return redirect("/recipes/")

        else:
            form = forms.RecipeForm()
    # recipe_list = models.RecipeModel.objects.all()

    recipeContext = {
        "title":"Recipe - Foodfficient",
        "pageTitle":"Add a recipe to  Foodfficient!",
        "body":"",
        "body2":"",
    }
    return render(request, "addRecipe.html", context=recipeContext)
