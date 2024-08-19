# The purpose of this exercise is to save a JSON in JS, Using a library called FileSaver and putting in the head of HTML.

import json
import os

# Read the JSON data from the file
file_path = 'quotes.json'

with open(file_path, 'r') as file:
    quotes = json.load(file)


# Convert the list to a JSON string with proper formatting
json_string = json.dumps(quotes, indent=2)

# Split the JSON string into individual objects
split_json = json_string.split('\n  },\n')

print(split_json)
