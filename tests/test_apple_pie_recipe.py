from lib.apple_pie_recipe import ApplePieRecipe

def test_apple_pie_recipe_instantiates():
    recipe = ApplePieRecipe()

    assert recipe.ingredients == ['apple', 'flour', 'sugar']

def test_apple_pie_lists_ingredients():
    recipe = ApplePieRecipe()

    assert recipe.list_ingredients() == 'apple, flour, sugar'
