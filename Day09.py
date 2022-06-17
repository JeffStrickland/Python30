"""
Day 09 - Enumerate

Create a list of 5 names and use the enumerate function to
display them as follows:
1. Name One
2. Name Two
...
5. Name Five
"""
name_list = ['Alex', 'Sarah', 'Jessica', 'Ellen', 'Binh']

for counter, element in enumerate(name_list):
    print(counter, element)
# ---> 
# 0 Alex
# 1 Sarah
# 2 Jessica
# 3 Ellen
# 4 Binh

"""
Use the enumerate function on a string (your name) and print
each character with its corresponding index
"""

for index, element in enumerate('Jeff'):
    print(index, element)
# --->
# 0 J
# 1 e
# 2 f
# 3 f