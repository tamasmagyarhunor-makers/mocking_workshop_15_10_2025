class PastryChefHunor():
    def __init__(self):
        self.name = "Hunor"
        self.favourite_food = 'Macaroni with tomato sauce and meatballs 3000kcal for the win'
    
    def bake(self, recipe):
        ingredients = recipe.list_ingredients()
        return f"I'm {self.name} and I baked an Apple Pie with " + ingredients + "!"