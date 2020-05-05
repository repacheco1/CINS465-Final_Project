from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.views import generic
from django.db import transaction
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.models import User
from . import (forms, models)
from .models import Recipe, Blog, Profile
from .forms import CommentForm, RecipeForm, BlogForm


def logoutPageView(request):
    logout(request)
    return redirect("/")

def homePageView(request):
    total_recipes = Recipe.objects.count()
    total_users = User.objects.count()
    indexContext = {
        "title":"Home - Foodfficient",
        "pageTitle":"Welcome to Foodfficient!",
        "total_recipes": total_recipes,
        "total_users": total_users,
    }
    return render(request, "index.html", context=indexContext)

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
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
            # print("Hi")
    else:
        form = forms.RegistrationForm()
    registerContext = {
        "title":"Registration - Foodfficient",
        "pageTitle":"Welcome to Foodfficient! Start by creating an account.",
        "form":form,
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

class SearchResultsView(generic.ListView):
    model = Recipe
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Recipe.objects.filter(
            Q(name__icontains=query) | 
            Q(ingredients__icontains=query) | 
            Q(total_time__icontains=query)
        ).order_by('-created_on')
        return object_list

class ProfileList(generic.ListView):
    queryset = Profile.objects.filter().order_by('user__date_joined')
    paginate_by = 20
    template_name = "profiles.html"

class ProfileDetails(generic.DetailView):
    model = Profile
    template_name = "profile_details.html"

class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter().order_by('-created_on')
    paginate_by = 12
    template_name = "recipes.html"

class RecipeDetails(generic.DetailView):
    model = Recipe
    template_name = "recipe_details.html"

class BlogList(generic.ListView):
    queryset = Blog.objects.filter().order_by('-published_on')
    paginate_by = 10
    template_name = "blog.html"

# class BlogDetails(generic.DetailView):
#     model = Blog
#     template_name = "blog_details.html"

def blogDetailsPageView(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.filter()
    new_comment = None
    if request.method =="POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.entry = blog
            new_comment.save()
    else:
        form = CommentForm()

    commentContext = {
        "blog": blog,
        "comments": comments,
        "new_comment": new_comment,
        # "rec_id" = rec_id,
        "form":form
    }
    return render(request, "blog_details.html", context=commentContext)


def chatPageView(request):
    return render(request, 'chat/index.html')

def chatRoomPageView(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

@login_required

def addRecipePageView(request):
    # form = forms.RecipeForm(data=request.POST, files=request.FILES)
    if request.method =="POST":
        form = forms.RecipeForm(data=request.POST, files=request.FILES)
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



@staff_member_required
def addBlogPageView(request):
    if request.method =="POST":
        form = forms.BlogForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.author = request.user
            new_entry.save()
            form = BlogForm()

    else:
        form = forms.BlogForm()

    addContext = {
        "title":"Add Blog Entry - Foodfficient",
        "pageTitle":"Welcome! Add a blog entry to Foodfficient!",
        "body":"",
        "body2":"",
        "form":form
    }
    return render(request, "add_blog.html", context=addContext)

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