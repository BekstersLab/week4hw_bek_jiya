# What is wrong with this code?
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'
print(cheese)
# prints: ['Cheddar', 'Stilton', 'Cornish Yarg', 'O', 'k', 'e']
# the string is split into characters and each character added as an individual item to the list
# works if you add a list item eg. cheese += ['Oke']

cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print(cheese)
cheese.append('Oke')
print(cheese)
# prints: ['Cheddar', 'Stilton', 'Cornish Yarg', 'Oke']

# How would you add two new cheeses to the list with a single command?
# issue - .append() method above can only add a single item
# .extend() method can add multiple items.
new_cheese = ['Brie', 'Emmental']
cheese.extend(new_cheese)
print(cheese)

# alternative is:
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += ['Brie', 'Emmental']
print(cheese)