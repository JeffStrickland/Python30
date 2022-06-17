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

### Refactored Using Lambdas

print(list(filter(lambda user: user['age'] < 18, users)))
# ---> [{'name': 'Jose', 'age': 15}]

"""
Create a new list of numbers in this case from -10 to
10 and return only those that are multiples of 3 and
negative.
"""

def by_3(x):
    return x % 3 == 0 and x < 0

newlist = list(range(-10, 11, 1))

print(list(filter(by_3, newlist)))
# ---> [-9, -6, -3]

### Refactored Using Lambdas

print(list(filter(lambda num: num % 3 == 0 and num < 0, newlist)))
# ---> [-9, -6, -3]

"""
Reduce
"""
from functools import reduce
"""
Day 06 - Reduce

Create a function that multiplies a sequence of
numbers.
"""

sequence = [2, 5, 7, 9, 4, 1]

def mult(x, y):
    return x * y

print(reduce(mult, sequence))
# ---> 2520
# ---> 2*5=10, 10*7=70, 70*9=630, 630*4=2520, 2520*1=2520

### Refactored Using Lambdas

print(reduce(lambda x, y: x * y, sequence))
# ---> 2520

"""
Create a function that takes a list of
strings and return the sum of its characters.
["I", "am", "esteban"] => 1 2 and 7
10
"""


x = ['I', 'am', 'Jeff']

def sum_char(a, b):
    if isinstance(a, str):
        a = len(a)
    else:
        a
    return a + len(b)

print(reduce(sum_char, x))
# ---> 7

### Refactored Using Lamdas

print(reduce(lambda word_a, word_b: (len(word_a) if isinstance(word_a, str) else word_a) + len(word_b), x))
# ---> 7

"""
This challenge can be a bit complicated, however
remember that in the functions you can perform
conditionals, take a list of numbers and return
the largest number.
"""

a = [1, 2, 3, 4, 5, 6, 7, 8]

def largest(x, y):
    max = x
    if y > max:
        max = y
    return max

print(reduce(largest, a))
# ---> 8

### Refactored Using Lambdas
print(reduce(lambda num_a, num_b: num_a if num_a > num_b else num_b, a))
# ---> 8