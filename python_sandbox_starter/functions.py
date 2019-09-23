# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create a function
def sayHello(name='Sam'): # we can also set a default like in this line, then we don't have to put a default parameter in line 7
  print(f'Hello {name}')

# sayHello()
# def getSum(num1, num2):
#   total = num1 + num2
#   return total

# num = getSum(3,4)
# print(num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2 # here the colon is like the arrow in JS

print(getSum(10, 3))
