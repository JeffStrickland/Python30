"""
Day 11 - Classmethod and Staticmethod

Create a class called Pizza that allows you to create different
types of them. When you create them, give them the price of the
pizza.
The class should calculate the size of the pizza based on the
price.
0 - 10 small
11 - 20 medium
21 - 30 large
"""

class Pizza:
    def __init__(self, ingredients, price):
        self.ingredients = ingredients
        self.price = price 
        self.size = self.pie_size(price)

    @staticmethod
    def pie_size(price):
        sizes = {'small': (0, 10), 'medium':(11, 20), 'large': (21, 30)}

        pie_size_x = ""
        for size, (min_price, max_price) in sizes.items():
            if min_price <= price <= max_price:
                pie_size_x = size
                break

        return pie_size_x

    @classmethod
    def pep(cls, price):
        ingredients = ['cheese', 'pepperoni']
        return cls(ingredients, price)

    @classmethod
    def shrimp(cls, price):
        ingredients = ['cheese', 'shrimp', 'basil', 'capers']
        return cls(ingredients, price)

    @classmethod
    def veg(cls, price):
        ingredients = ['cheese', 'pepper', 'mushroom', 'olive', 'basil','eggplant']
        return cls(ingredients, price)

pepperoni = Pizza.pep(5)
shrimp = Pizza.shrimp(15)
vegetable = Pizza.veg(30)

print(pepperoni.size, pepperoni.ingredients)
print(shrimp.size, shrimp.ingredients)
print(vegetable.size, vegetable.ingredients)
# --- > 
# small ['cheese', 'pepperoni']
# medium ['cheese', 'shrimp', 'basil', 'capers']
# large ['cheese', 'pepper', 'mushroom', 'olive', 'basil', 'eggplant']

