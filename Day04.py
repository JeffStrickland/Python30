"""
Day 04 - Map

Again use the range function to generate a sequence of
numbers from 1 to 20, use the map function to return
whether the number is even or not.
"""
#_____________________________________________________________
def even_num(number):
    return (number % 2 == 0)

print(list(map(even_num, range(1, 10))))
# --> False, True, False, True, False, True, False, True, False]
#_______________________________________________________________
"""
Create two lists A and B of numbers, which must be given
to the function, the final result will be a new list which
will contain the sum of the values in A and B
A = [1, 5, 6]
B = [3, 5, 9]
C = [4, 10, 15]
"""
#__________________________________________
A = [1, 5, 6]
B = [3, 5, 9]

def sum_lists(x, y):
    return x + y

print(list(map(sum_lists, A, B)))
# ---> [4, 10, 15]
#_________________________________________
"""
Create a list of lists, these with multiple numbers to
be averaged
[
    [1, 2, 3],
    [9, 6, 1]
]
"""
#__________________________________________
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
#__________________________________________