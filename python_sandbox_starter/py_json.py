# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON

userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# parse to dictionary
user = json.loads(userJSON)
print(user)

# Just getting one property
print(user['first_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(car) # converting dictionary to JSON format

print(carJSON)