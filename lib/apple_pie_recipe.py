class ApplePieRecipe():
    def __init__(self):
        self.ingredients = ['apple', 'flour', 'sugar']

    def list_ingredients(self):
        return ", ".join(self.ingredients)