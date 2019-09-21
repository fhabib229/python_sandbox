# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members. Very similar to an object literal in JS

# Create a dictionary
person = {
  'first_name': 'John', # Keys are in quotes
  'last_name': 'Doe',
  'age': 30
}
#print(person, type(person))

# Use a constructor
# person2 = dict(first_name='Sarah', last_name='Williams')

# Access a single value
# print(person['first_name']) # more common way
# print(person.get('first_name'))

# Add key/value
person['phone'] = '123-456-7890'

print(person)

# Get dictionary keys
print(person.keys())

# get dictionary items
print(person.items())

# copy dictionary

person2 = person.copy() # similar to spread operator in Javascript
person2['city'] = 'Seattle'
print(person2)

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()
print(person)

# Get length
print(len(person2))

# List of dictionaries, like an array of objects in JS
people = [
  {'name': 'Martha', 'age': 30},
  {'name': 'Kevin', 'age': 25}
]

print(people)

# Getting a specific key/value from a list of dictionaries
print(people[1]['name'])
