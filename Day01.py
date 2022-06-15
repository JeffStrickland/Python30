"""
Day 01 - *args and **kwargs

Create a function that receives N numbers and returns
each of these multiplied by 2
"""

# *args
def multiply_by_two(*numbers):
    results = []
    for i in numbers:
        results.append(i * 2)

    return results

 # Test it out  
print(multiply_by_two(5, 9, 6, 3, 8, 15, 8, 6, 23, 1))
# ---> [10, 18, 12, 6, 16, 30, 16, 12, 46, 2]
print(multiply_by_two(5, 85, 9))
# ---> [10, 170, 18]

"""
Create a function that receives N arguments with your
personal information: name, age, phone, country, etc
Then print those values with their names
name: your name
country: your country
"""

# **kwargs
def personal_information(**info):
    for key, x in info.items():
        print(f'{key}: {x}')

personal_information(name="Esteban",
    lastname="Solorzano",
    age=26,
    country="Colombia")
# --->
# name: Esteban
# lastname: Solorzano
# age: 26
# country: Colombia

"""
The Python print function receives positional and named arguments,
the named arguments are used to alter the way this print works:
sep = It indicates how all the values we pass will be separated
end = Indicates what you will put at the end of printing
Default Values:
sep = " "
end = "\n"
Use the *args and **kwargs to pass these arguments and print a phrase
depending on a tuple/list of values.
"""

print()