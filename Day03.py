"""
Day 03 - List Slices

You can use the range function to easily create a list with
100 numbers, use list slices to take only those numbers that
are multiples of 3.
"""

x = list(range(1,101))
new_x = list[2::3]
print(x[2::3])
# ---> [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 
# 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

"""
From the list
['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
Generate the following
['o', 'l', 'l']
"""

hello = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
print(hello[4:1:-1])
# --> ['o', 'l', 'l']

"""
Remember it doesn't only work with lists, write your name and
put it in reverse
"""

name = 'Jeff'
print(name[::-1])
# --> ffeJ

