"""
Day 15 - Else

Use for/else or while/else to validate all numbers in a
list and print out whether or not there is an even number.
"""

list_of_numbers = [1, 2, 3, 4, 5, 6]
list_of_other_numbers = [1, 3, 5]

def validation(x):
    y = []
    for i in x:
        if i % 2 == 0:
            y.append(i)      
        else:
            pass
    if len(y) > 0:    
        return (f'List of even numbers {y}')
    else:
        return (f'No even numbers in the list')

print(validation(list_of_numbers))
# ---> List of even numbers [2, 4, 6]
print(validation(list_of_other_numbers))
# ---> No even numbers in the list

"""
Create a random number from 1 to 10 and by using a for/else
or while/else allow the user to enter their options, win if
the user guess it, lose after 3 attempts.
"""

import random

# Random number generation
random_num = random.randint(1, 10)
# 3 attemps
# Driver
def main():
    random_num = random.randint(1, 10)
    loop = 3
    while loop > 0:
        guess = int(input("Guess a number.  You get 3 attemps!"))
        if guess == random_num:
            print("Correct")
            break
        loop -= 1

    else:
        print(f'The number was {random_num}')

if __name__ == "__main__":
    main()
