"""

Day 17 - Memoization

Memoization is not really difficult, find any other simple
example that you can implement memoization to not repeat processes.
"""

from timeit import timeit

def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    return fibonacci(x - 1) + fibonacci(x - 2)

print(timeit("fibonacci(35)", setup ="from __main__ import fibonacci", number=1))
print(fibonacci(35))
# ---> 5.906693763
# ---> 9227465