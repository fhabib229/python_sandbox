# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# Create tuple w/ constructor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# If you only have one value in a tuple, you want to leave a trailing comma
# fruits2 = ('Apples')
fruits2 = ('Apples', ) # now it's a tuple

print(fruits2, type(fruits2)) # Because there is no trailing comma on line 9, the type is classified as a string



# A Set is a collection which is unordered and unindexed. No duplicate members.
