from django import forms
from .models import Recipes

class RecipeSearchForm(forms.Form):
    recipe_difficulty = forms.ChoiceField(
        choices=[('', 'Choose a difficulty level')] + list(Recipes.DIFFICULTY_CHOICES)
    )
    chart_type = forms.ChoiceField(choices=[
        ('#1', 'Bar chart'),
        ('#2', 'Pie chart'),
        ('#3', 'Line chart')
    ])

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['name', 'description', 'pic', 'ingredients', 'difficulty', 'cooking_time']