class ApplePieRecipe():
    def __init__(self):
        self.ingredients = ['apple', 'flour', 'sugar', 'lemon zest']

    def list_ingredients(self):
        return ", ".join(self.ingredients)