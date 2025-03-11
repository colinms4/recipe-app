from django.db import models

# Create your models here.

class Recipes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    difficulty = models.CharField(max_length=50, choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')])
    cooking_time = models.IntegerField(help_text="Cooking time in minutes")

    def __str__(self):
        return self.name
