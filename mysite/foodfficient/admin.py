from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from . import models

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'total_time', 'author', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'ingredients', 'optional_ingredients', 'substitutions')
    prepopulated_fields = {'slug': ('name',)}

class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'published_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'entry', 'published_on')
    list_filter = ('published_on',)
    search_fields = ('author', 'entry', 'body')

# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Comment, CommentAdmin)
