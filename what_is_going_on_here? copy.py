#COLLECTIONS

# what is going on here?
# can you explain the output?

tup = 'hello'
print(len(tup))
# by writing the variable as tup, it is confusing us
# it tricks us into thinking it is a tuple where it is only a variable holding a string
# lens prints the length of the tuple which is only 5
tup = 'hello',
print(len(tup))
# it prints the length of the data on the tuple
#in the first example it prints tup as a string and in the second
# because there is a comma, it makes a tuple, so it tells us the elements in the tuple


# use the python() help function?