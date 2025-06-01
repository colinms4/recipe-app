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
        self.assertEqual(recipe.get_absolute_url(), f"/recipes/list/1")
