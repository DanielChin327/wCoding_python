# The purpose of this exercise is to save a JSON in JS, Using a library called FileSaver and putting in the head of HTML.

import json


# Read the JSON data from the file
file_path = 'quotes.json'

with open(file_path, 'r') as file:
    quotes = json.load(file)
print("this is json.load: ")
print(quotes)

# Convert the list to a JSON string with proper formatting
json_string = json.dumps(quotes, indent=2)
print("this is json.dumps: ")
print(json_string)

# Split the JSON string into individual objects
split_json = json_string.split('\n  },\n')

print(split_json)



# Explanation of the Code:
#
# 1. import json:
#    - This statement imports the built-in json module, allowing the use of functions to work with JSON data.
#    - JSON (JavaScript Object Notation) is a lightweight data-interchange format.
#
# 2. json.load(file):
#    - This function reads JSON data from a file-like object (in this case, the opened file) and parses it into a Python dictionary or list.
#    - In the code, it reads the contents of 'quotes.json' and stores it in the 'quotes' variable as a Python object.
#
# 3. json.dumps(quotes, indent=2):
#    - This function converts a Python object (such as a dictionary or list) into a JSON-formatted string.
#    - The indent=2 argument formats the JSON string with 2 spaces of indentation for better readability.
#    - The resulting JSON string is stored in the 'json_string' variable.
#
# 4. split_json = json_string.split('\n  },\n'):
#    - This line splits the JSON string into individual objects based on the pattern '\n  },\n'.
#    - This is useful if you need to manipulate or inspect each JSON object separately.
