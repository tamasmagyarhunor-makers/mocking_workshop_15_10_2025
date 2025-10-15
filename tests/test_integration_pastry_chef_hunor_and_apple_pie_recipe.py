from lib.pastry_chef_hunor import PastryChefHunor
from lib.apple_pie_recipe import ApplePieRecipe

def test_integration_pastry_chef_hunor_can_bake_apple_pie():
    hunor = PastryChefHunor()
    recipe = ApplePieRecipe()


    assert hunor.bake(recipe) == "I'm Hunor and I baked an Apple Pie with apple, flour, sugar, lemon zest!"