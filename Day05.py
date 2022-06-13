"""
Day 05 - Filter

Using the range function, create a sequence of numbers
from 1 to 100, and using the filter function return only
those that are multiplies of 2.
"""
#________________________________________
def by_2(x):
    return x % 2 == 0

sequence = list(range(1, 101, 1))

print(list(filter(by_2, sequence)))
# ---> 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 
# 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 
# 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 
# 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
#______________________________________________________
"""
According to the example of older users, take the same
list of users or create your own and return those who
are underage.
"""
#____________________________________________
users = [
    {
        "name": "Esteban",
        "age": 26
    },
    {
        "name": "Jose",
        "age": 15
    },
    {
        "name": "Jaime",
        "age": 18
    }
]

def validate_age(user):
    return user["age"] < 18

print(list(filter(validate_age, users)))
# ---> {'name': 'Jose', 'age': 15}]
#____________________________________________
"""
Create a new list of numbers in this case from -10 to
10 and return only those that are multiples of 3 and
negative.
"""
#_______________________________________________

def by_3(x):
    return x % 3 == 0

newlist = list(range(-10, 11, 1))

print(list(filter(by_3, newlist)))
# ---> [-9, -6, -3, 0, 3, 6, 9]
#_______________________________________________