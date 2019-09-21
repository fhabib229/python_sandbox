# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# Create tuple w/ constructor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# If you only have one value in a tuple, you want to leave a trailing comma
# fruits2 = ('Apples')
fruits2 = ('Apples', ) # now it's a tuple

# print(fruits2, type(fruits2)) # Because there is no trailing comma on line 9, the type is classified as a string

# Retrieving a single value
print(fruits[1]) # like lists or arrays, tuples are zero-index-based

# Remember, you can't change the values
# fruits[0] = 'Pears'

# Here's the error : Traceback (most recent call last):
#   File "tuples_sets.py", line 18, in <module>
#     fruits[0] = 'Pears'
# TypeError: 'tuple' object does not support item assignment

# Deleting a tuple
del fruits2
# print(fruits2)

# Get length
len(fruits)

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create a set
fruits_set = {'Apples', 'Oranges', 'Mango'}