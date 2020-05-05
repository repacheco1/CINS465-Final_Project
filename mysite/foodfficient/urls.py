from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.registerPageView, name='register'),
    path('users/', views.ProfileList.as_view(), name='profile'),
    path('edit-profile/', views.editProfilePageView, name='edit_profile'),
    path('users/<slug:slug>/', views.ProfileDetails.as_view(), name='profile_details'),
    path('add-recipe/', views.addRecipePageView, name='add_recipe'),
    path('logout/', views.logoutPageView, name='logout'),
    path('about/', views.aboutPageView, name='about'),
    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    # path('recipes/<slug:slug>/', views.recipeDetailPageView, name='recipe_details'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('add-blog/', views.addBlogPageView, name='add_blog'),
    path('blog/', views.BlogList.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.blogDetailPageView, name='blog_details'),
    path('summernote/', include('django_summernote.urls')),
    path('recipe/<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_details'),
    # path('comments/', include('django_comments_xtd.urls')),
    # path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('friendship/', include('friendship.urls')),
    # path('recipes/', views.recipesPageView, name='Recipes'),
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)