from django.test import TestCase
from .models import Recipes

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

    def test_recipe_creation(self):
        """Test if the recipe is created successfully"""
        self.assertEqual(self.recipe.name, "Spaghetti Carbonara")
        self.assertEqual(self.recipe.ingredients, "Spaghetti, Eggs, Cheese, Bacon, Pepper")
        self.assertEqual(self.recipe.difficulty, "Medium")
        self.assertEqual(self.recipe.cooking_time, 30)

    def test_str_representation(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.recipe), "Spaghetti Carbonara")