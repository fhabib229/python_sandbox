# A class is like a blueprint for creating objects.
# An object has properties and methods(functions) associated with it.
# Almost everything in Python is an object
# Just like JS es6 classes

# Create class
class User:
  # Constructor
  def __init__(self, name, email, age):
    self.name = name # in other languages you would use this (like es6), but in python you use self
    self.email = email
    self.age = age
  # Creating a method

  def greeting(self): # this
    return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
    self.age += 1
# Init user object
faris = User('Faris Habib', 'faris@hello.net', 27)

# Extending class
class Customer(User):
  # Constructor
  def __init__(self, name, email, age):
    self.name = name # in other languages you would use this (like es6), but in python you use self
    self.email = email
    self.age = age
    self.balance = 0

  def set_balance(self, balance):
    self.balance = balance

  # this will override the greeting method from the User class in the Customer class only
  def greeting(self): # this
    return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# Init customer object
janet = Customer('Janet Johnson', 'janet@yahoo.com', '25')

janet.set_balance(500)
print(janet.greeting())
print(type(faris))

# Accessing the properties
#print(faris.name)

#calling birthday to add 1 to age
faris.has_birthday()
print(faris.greeting())