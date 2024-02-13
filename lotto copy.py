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

