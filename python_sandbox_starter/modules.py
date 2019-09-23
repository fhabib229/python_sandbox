# A module is basically a file containing a set of functions to include in your application.
# There are core python modules, modules you can install using the pip package manager (including Django)
# as well as custom modules

# core modules
import datetime
# today = datetime.date.today() # Lookup the documentation for datetime to see all available properties
# print(today)

# # Can also just import date
# from datetime import date
# today = date.today()
# print(today)

# importing time
# import time
# timestamp = time.time()
# print(timestamp)

# the example above is not formatted neat, so we can do this instead
# from time import time
# timestamp = time()
# print(timestamp)

# importing the camelcase we just installed
# pip module
# from camelcase import CamelCase
# c = CamelCase()
# print(c.hump('hello there world'))

# Importing the custom validator module from validator.py
import validator
# or could do below
from validator import validate_email

email = 'test@hello.com'
if validate_email(email):
  print('Email is valid')
else:
  print('Not a valid Email')