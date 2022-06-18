"""
Day 13 - Dunder Methods
"""
# Class created on Day 11

class Pizza:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price 
        self.size = self.pie_size(price)

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, ingredient):
        self.__ingredients = ingredient

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def size(self):
        return self.__size

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

    def __repr__(self):
        return f"Pizza {self.__name}"

    def __contains__(self, ingredient):
        return ingredient in self.__ingredients
    
    def __len__(self):
        return len(self.__ingredients)