# COLLECTIONS
# Objective: write a python script that will generate and display 6 unique random lottery numbers between 1 and 50.
# Think about which data structure is best suited to store the numbers.
# Use the Python help() function to find out which function to use from the python standard library called random.

import random
# the important statement, which is orange showing it is a statement
# The random module in Python defines a series of functions for
# generating or manipulating random integers. The import random loads the random module,
# which contains a number of random number generation-related functions.
lottery_numbers = random.sample(range(1, 51), 6)
# what does sample do? The sample, allows us to get the numbers from the random statement
# what does range do? it gives us the range of what is being pulled, in this case we wanted 6 numbers
print(lottery_numbers)

# //////////////////////////

# solution 2
# create an empty list to store the numbers in
numbers_list = []

# use a range of 6 in a for loop - loops 6 times to generate 6 numbers
for i in range(6):
    while True:
        # generate a random number between 1 and 50
        number = random.randint(1, 50)
        # checks if number already in list
        if number not in numbers_list:
            # if not in list (new number) then add to the list
            numbers_list.append(number)
            # break out of while loop
            break
# code loops back round through for loop until 6 unique numbers have been added to the list

# sort the list in ascending order
numbers_list.sort()
# print the list
print(numbers_list)
