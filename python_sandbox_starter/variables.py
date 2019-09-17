# A variable is a container for a value, which can be of various types

'''
This is a
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# main data types
x = 1 # int
y = 2.5 # float point number
name = 'Bob' # str, can have single or double quotes
is_cool = True # bool, must be capitalized, otherwise would be looked at as a variable

# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'Bob', True) # Does the same thing as lines 18 - 21 but more compact

# Basic Math
a = x + y

# Casting
x = str(x)
y = int(y)
# Changing y back to a float
z = float(y)

print('Hello World!')

print(x, y, name, is_cool, a)

print(type(y), y) # y will print out 2 instead of 2.5 since this is now an int (whole number)

print(type(z), z) # now it's 2.0