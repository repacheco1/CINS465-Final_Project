from django.db import models

class RecipeModels(models.Model):
    recipe_name = models.CharField(max_length=50)
    recipe_time = models.IntegerField()
    recipe_description = models.TextField()
    recipe_ingredients = models.TextField()
    recipe_instructions = models.TextField()

    def __str__(self):
        return self.recipe_name