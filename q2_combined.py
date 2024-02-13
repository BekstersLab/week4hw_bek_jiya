# What is going on here? Can you explain the output?

tup = 'Hello'
print(len(tup))
# tup is assigned string value.
# Using len function returns number of characters in the string
# prints: 5

tup = 'Hello',
print(len(tup))
# addition of comma means tup doesn't contain a string, but a tuple containing a single string item.
# len now counts the number of strings in the tuple
# prints: 1