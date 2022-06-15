"""
Day 02 - Range

Generate a sequence using the function range that
returns the following.
[-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0,
10, 20, 30, 40, 50, 60, 70, 80, 90]
"""

sequence = list(range(-100, 100, 10))
print(sequence)
# ---> [-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

"""
Generate the previous sequence but in this case in
the opposite way.
"""

sequence = list(range(90, -110, -10))
print(sequence)
# ---> [90, 80, 70, 60, 50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100]

"""
This challenge can be a bit difficult, try to create a
function that returns a sequence of decimal numbers between
2 numbers, incremental only.
Here's a hint, use the while statement
"""

def floating_range(start, stop, step):
    sequence = []
    x = start
    if x < stop:
        while x < stop:
            sequence.append(x)
            x += step
            x = round(x, 2)
    else:
        while x > stop: 
            sequence.append(x)
            x += step
            x = round(x, 2)
    return sequence

print(floating_range(1, 2.1, .1))
# ---> [1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
print(floating_range(1, -1.2, -.2))
# ---> [1, 0.8, 0.6, 0.4, 0.2, 0.0, -0.2, -0.4, -0.6, -0.8, -1.0]
