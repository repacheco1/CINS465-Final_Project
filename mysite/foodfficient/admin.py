from django.contrib import admin
from . import models

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'total_time', 'author', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'ingredients', 'optional_ingredients', 'substitutions')
    prepopulated_fields = {'slug': ('name',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'recipe', 'published_on')
    list_filter = ('published_on',)
    search_fields = ('author', 'recipe', 'body')

# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Comment, CommentAdmin)