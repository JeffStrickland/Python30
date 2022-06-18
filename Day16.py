"""
Day 16 - Recursion

Create a recursive function which calculates the
factorial of a given number
Factorial: factorial(5) => 1*2*3*4*5 => 120
3 => 6
5 => 120
7 => 5040
10 => 3628800
"""
def find_factorial(x):
    if x == 1:
        return x
    return x * find_factorial(x - 1)

print(find_factorial(3))
# ---> 6

"""
Let's simulate the operation of the operator module (%).
4 % 2 => 0
59 % 6 => 5
"""
def modulo(x, y):
    if x < y:
        return x
    return modulo(x - y, y)

print(modulo(59, 6))
# --> 5
print(59 % 6)
# ---> 5
