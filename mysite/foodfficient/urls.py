from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.homePageView, name='Home'),
    path('profile/', views.profilePageView, name='Profile'),
    path('login/', auth_views.LoginView.as_view(), name='Login'),
    path('register/', views.registerPageView, name='Register'),
    path('addRecipe/', views.addRecipePageView, name='Add Recipe'),
    path('logout/', views.logoutPageView, name='Logout'),
    path('about/', views.aboutPageView, name='About'),
    path('recipes/', views.recipePageView, name='Recipes')
]