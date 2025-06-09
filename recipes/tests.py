from django.test import TestCase
from .models import Recipes
from django.test import TestCase, Client
from django.urls import reverse
from .forms import RecipeSearchForm
from .views import records
from django.contrib.auth.models import User


# Create your tests here.

class RecipesModelTest(TestCase):
    def setUp(self):
        """Set up a test recipe before each test"""
        self.recipe = Recipes.objects.create(
            name="Spaghetti Carbonara",
            ingredients="Spaghetti, Eggs, Cheese, Bacon, Pepper",
            difficulty="Medium",
            cooking_time=30
        )

    def test_str_representation(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.recipe), "Spaghetti Carbonara")

    
    def test_create_recipe(self):
        recipe = Recipes.objects.create(
            name="Spaghetti Carbonara",
            ingredients="Spaghetti, Eggs, Pancetta, Parmesan",
            difficulty="Medium",
            cooking_time=30,
            description="A classic Italian pasta dish."
        )
        self.assertEqual(recipe.name, "Spaghetti Carbonara")
        self.assertEqual(recipe.difficulty, "Medium")
        self.assertIn("Pancetta", recipe.ingredients)
        self.assertEqual(str(recipe), "Spaghetti Carbonara")

    def test_get_absolute_url(self):
        recipe = Recipes.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), f"/list/1/")


class RecipeFormTest(TestCase):

    def test_form_valid_with_correct_data(self):
        form_data = {
            'recipe_difficulty': Recipes.DIFFICULTY_CHOICES[0][0],  
            'chart_type': '#1',  
        }
        form = RecipeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_with_empty_fields(self):
        form_data = {
            'recipe_difficulty': '',  
            'chart_type': '',        
        }
        form = RecipeSearchForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('recipe_difficulty', form.errors)
        self.assertIn('chart_type', form.errors)

    def test_recipe_difficulty_field_required(self):
        form = RecipeSearchForm(data={'recipe_difficulty': '', 'chart_type': '#1'})
        self.assertFalse(form.is_valid())
        self.assertIn('recipe_difficulty', form.errors)

    def test_chart_type_field_required(self):
        form = RecipeSearchForm(data={'recipe_difficulty': Recipes.DIFFICULTY_CHOICES[0][0], 'chart_type': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('chart_type', form.errors)
