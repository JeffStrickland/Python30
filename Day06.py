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