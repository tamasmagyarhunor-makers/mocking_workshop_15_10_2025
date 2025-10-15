from lib.pastry_chef_hunor import PastryChefHunor
from lib.apple_pie_recipe import ApplePieRecipe
from unittest.mock import Mock

def test_pastry_chef_hunor_instantiates():
    hunor = PastryChefHunor()

    assert hunor.name == 'Hunor'
    assert hunor.favourite_food == 'Macaroni with tomato sauce and meatballs 3000kcal for the win'

def test_pastry_chef_hunor_can_bake_apple_pie():
    hunor = PastryChefHunor()
    recipe = ApplePieRecipe()

    assert hunor.bake(recipe) == "I'm Hunor and I baked an Apple Pie with apple, flour, sugar!"




























    # mock_object = Mock
    # mock_object.function_call.return_value = 'whatever I want'