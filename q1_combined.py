#COLLECTIONS

cheese = ['cheddar', 'stilton', 'cornish yarg']
cheese += 'oke'

# How should 'oke' be added to the end of the cheese list?

cheese.append('oke')
# the method .append to the variable adds onto the end of the list
# .append only takes one argument, can't add two cheeses using this
print(cheese)

# How would you add two new cheeses to the list with a single command?

# can use .extend but not with a single command - example below
new_cheese = 'oke', 'mozzarella'
cheese.extend(new_cheese)
print(cheese)

# alternative method is:
# Fixes the original issue - += works if adding item(s) as a list
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += ['Brie', 'Emmental']
print(cheese)