from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views
from django.conf.urls.static import static
# from .views import RecipeListView

urlpatterns = [
    path('', views.homePageView, name='Home'),
    path('profile/', views.profilePageView, name='Profile'),
    path('login/', auth_views.LoginView.as_view(), name='Login'),
    path('register/', views.registerPageView, name='Register'),
    path('add-recipe/', views.addRecipePageView, name='Add Recipe'),
    path('logout/', views.logoutPageView, name='Logout'),
    path('about/', views.aboutPageView, name='About'),
    path('recipes/', views.recipesPageView, name='Recipes'),
]+ static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)