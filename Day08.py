"""
Day 08 - Comprehensions

Create a list of words and with it, create a new dictionary
in which the key is the word and the value is the same word
reversed.
"""
words = ['test', 'new', 'list', 'comprehension']
new_dictionary = {word: word[::-1] for word in words}
print(new_dictionary)
# ---> {'test': 'tset', 'new': 'wen', 'list': 'tsil', 'comprehension': 'noisneherpmoc'}
"""
Let's try this one again:
Using the range function, create a sequence of numbers
from 1 to 100, and using the comprehension to return only
those that are multiplies of 2.
"""
my_list = list(range(1, 101, 1))
x = [num for num in my_list if num % 2 == 0]
print(x)
# ---> [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 
# 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 
# 92, 94, 96, 98, 100]

"""
[[1, 2, 3, 4], [5, 6, 7, 8]]
Use the list above and create nested comprehensions so that
the final value is a new list like the following
[[2, 4, 6, 8], [10, 12, 14, 16]] The number multiplied by 2
"""
given_list = [[1, 2, 3, 4], [5, 6, 7, 8]]
new_list = [[num * 2 for num in num_list] for num_list in given_list]
print(new_list)
# ---> [[2, 4, 6, 8], [10, 12, 14, 16]]
