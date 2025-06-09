from django.db import models
from django.urls import reverse

# Create your models here.

class Recipes(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'), 
        ('Medium', 'Medium'), 
        ('Hard', 'Hard')
    ]
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)
    cooking_time = models.IntegerField(help_text="Cooking time in minutes")
    pic = models.ImageField(upload_to='recipes/', default='recipes/no_picture.jpg')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipes:recipes_detail', kwargs={'pk': self.pk})
