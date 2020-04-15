from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views import generic
from django.db import transaction
from django.http import JsonResponse
from datetime import datetime, timezone
from . import (forms, models)


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
    return render(request, "editProfile.html", context=editContext)


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

def recipesPageView(request):
    recipe_objects = models.Recipe.objects.all()
    recipe_list = []
    for rec in recipe_objects:
        comment_objects = models.Comment.objects.filter(recipe = rec)
        temp_rec = {}
        temp_rec["name"] = rec.name
        temp_rec["author"] = rec.author.username
        temp_rec["time"] = rec.time
        temp_rec["description"] = rec.description
        temp_rec["comments"]=comment_objects
        recipe_list+=[temp_rec]
        

    aboutContext = {
        "title":"Recipes - Foodfficient",
        "pageTitle":"Here is a list of recipes available at Foodfficient!",
        "body":"",
        "body2":"",
        "recipe_list":recipe_list,
    }
    return render(request, "recipes.html", context=aboutContext)
    

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
    return render(request, "addRecipe.html", context=addContext)

def commentPageView(request, rec_id):
    if not request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        if request.user.is_authenticated:
            form = forms.CommentForm(request.POST)
            if form.is_valid():
                form.save(request, rec_id)
                return redirect("/")
        else:
            form = forms.CommentForm()
    else:
        form = forms.CommentForm()
    commentContext = {
        "title":"Comment - Foodfficient",
        "pageTitle":"Add a comment!",
        "rec_id":rec_id,
        "form":form
    }
    return render(request,"comment.html", context=commentcontext)


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