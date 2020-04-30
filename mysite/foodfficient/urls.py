from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views
from django.conf.urls.static import static
# from .views import SearchResultsView

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.registerPageView, name='register'),
    path('profile/', views.profilePageView, name='profile'),
    path('edit-profile/', views.editProfilePageView, name='edit_profile'),
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
    path('recipe/<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_details'),
    # url(r'^reviews/', include('reviews.urls')),
    # path('recipes/', views.recipesPageView, name='Recipes'),
]+ static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)