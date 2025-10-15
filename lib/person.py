import random

class Person:
    def __init__(self, name):
        self.name = name
    
    def tries_to_go_out(self):
        weather = random.choice(['sunny', 'rainy'])

        if weather == 'sunny':
            return "It's sunny outside, let's take sunglasses and go out!"
        elif weather == 'rainy':
            return "It's rainy outside, let's take the umbrella and go out!"