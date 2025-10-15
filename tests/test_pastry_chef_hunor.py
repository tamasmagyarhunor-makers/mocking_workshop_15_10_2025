from lib.pastry_chef_hunor import PastryChefHunor
from unittest.mock import Mock

def test_pastry_chef_hunor_instantiates():
    hunor = PastryChefHunor()

    assert hunor.name == 'Hunor'
    assert hunor.favourite_food == 'Macaroni with tomato sauce and meatballs 3000kcal for the win'

def test_pastry_chef_hunor_can_bake_apple_pie():
    hunor = PastryChefHunor()

    recipe = Mock()
    recipe.list_ingredients.return_value = 'apple, flour, sugar, lemon zest'


    assert hunor.bake(recipe) == "I'm Hunor and I baked an Apple Pie with apple, flour, sugar, lemon zest!"

