"""
Day 07 - Lambdas

Use the lambda functions with the challenges of
map, filter and reduce.

MAP
Again use the range function to generate a sequence of
numbers from 1 to 20, use the map function to return
whether the number is even or not.
"""

def even_num(number):
    return (number % 2 == 0)

print(list(map(even_num, range(1, 10))))
# --> False, True, False, True, False, True, False, True, False]

### Refactored Using Lambdas

n1 = range(1, 10)
print(list(map(lambda number: number % 2 == 0, n1)))
# ---> [False, True, False, True, False, True, False, True, False]

"""
Create two lists A and B of numbers, which must be given
to the function, the final result will be a new list which
will contain the sum of the values in A and B
A = [1, 5, 6]
B = [3, 5, 9]
C = [4, 10, 15]
"""
A = [1, 5, 6]
B = [3, 5, 9]

def sum_lists(x, y):
    return x + y

print(list(map(sum_lists, A, B)))
# ---> [4, 10, 15]

### Refactored Using Lambdas

print(list(map(lambda x, y: x + y, A, B)))
# ---> [4, 10, 15]

"""
Create a list of lists, these with multiple numbers to
be averaged
[
    [1, 2, 3],
    [9, 6, 1]
]
"""

a = [
    [1, 2, 3],
    [9, 6, 1],
    [3, 4, 5],
    [7, 8, 1]
]

def av_list(x):
    y = sum(x)
    return round(y / len(x), 2)

print(list(map(av_list, a)))
# --> [2.0, 5.33, 4.0, 5.33]

### Refactored Using Lambdas

print(list(map(lambda x: round(sum(x) / len(x), 2), a)))
# ---> [2.0, 5.33, 4.0, 5.33]

"""
Filter
Using the range function, create a sequence of numbers
from 1 to 100, and using the filter function return only
those that are multiplies of 2.
"""

def by_2(x):
    return x % 2 == 0

sequence = list(range(1, 101, 1))

print(list(filter(by_2, sequence)))
# ---> 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 
# 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 
# 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 
# 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

### Refactored Using Lambdas

print(list(filter( lambda x: x % 2 == 0, sequence)))
# ---> 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 
# 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 
# 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 
# 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

"""
According to the example of older users, take the same
list of users or create your own and return those who
are underage.
"""

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

"""
Create a new list of numbers in this case from -10 to
10 and return only those that are multiples of 3 and
negative.
"""


def by_3(x):
    return x % 3 == 0

newlist = list(range(-10, 11, 1))

print(list(filter(by_3, newlist)))
# ---> [-9, -6, -3, 0, 3, 6, 9]"""

"""
Reduce
"""