# Write a Python script called lotto.py that will generate and display 6 unique random lottery numbers between 1 and 50
# Think about which Python data structure is best suited to store the numbers
# Use the Python help() function to find out which function to use from the python standard library called random

import random

# # solution 1 - wrong as same number can be called more than once
# numbers_list = []
#
# for i in range(6):
#     number = random.randint(1, 50)
#     numbers_list.append(number)
#
# print(numbers_list)


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