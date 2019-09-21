# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [ 1, 2, 3, 4, 5]

# Using a constructor, it's like JS, as if you're calling a new Array constructor.
numbers2 = list((1,2,3,4,5))

# print(numbers, numbers2)

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Get a single value from a list
print(fruits[1]) # lists are zero-based just like arrays, here we're getting oranges

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')


# Remove from list

fruits.remove('Grapes')


# Appending to list at a specific position

fruits.insert(2, 'Strawberries')

# Removing from a specific position
fruits.pop(2) # Strawberries is gone

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

# Change element/value
fruits[0] = 'Blueberries'

print(fruits)