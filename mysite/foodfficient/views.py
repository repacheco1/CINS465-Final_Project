from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views import generic
from django.db import transaction
from django.http import JsonResponse
from datetime import datetime, timezone
from . import (forms, models)
from .models import Recipe
from .forms import CommentForm


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

def editProfilePageView(request):
    # if request.method == "POST":
    #     form_instance = forms.ProfileForm(request.POST)
    #     if form_instance.is_valid():
    #         form_instance.save()
    #         return redirect("/profile/")
    #         # print("Hi")
    # else:
    #     form_instance = forms.ProfileForm
    editContext = {
        "title":"Edit Profile - Foodfficient",
        "pageTitle":"Edit Profile",
        "body":"",
        "body2":"",
    }
    return render(request, "edit_profile.html", context=editContext)


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

class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter().order_by('-created_on')
    template_name = "recipes.html"

class RecipeDetail(generic.DetailView):
    model = Recipe
    template_name = "recipe_details.html"
    
def recipeDetailPageView(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    comments = recipe.comments.filter()
    new_comment = None
    if request.method =="POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.recipe = recipe
            new_comment.save()
    else:
        form = CommentForm()
    commentContext = {
        "recipe": recipe,
        "comments": comments,
        "new_comment": new_comment,
        # "rec_id" = rec_id,
        "form":form
    }
    return render(request, "recipe_details.html", context=commentContext)

@login_required

def addRecipePageView(request):
    if request.method =="POST":
        form = forms.RecipeForm(request.POST)
        if form.is_valid():
            form.save(request)
            form = forms.RecipeForm()

    else:
        form = forms.RecipeForm()
    
    addContext = {
        "title":"Add Recipe - Foodfficient",
        "pageTitle":"Welcome! Add a recipe to Foodfficient!",
        "body":"",
        "body2":"",
        "form":form
    }
    return render(request, "add_recipe.html", context=addContext)



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