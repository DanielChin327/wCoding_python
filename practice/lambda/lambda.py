# Lambda functions are small, anonymous functions defined using the 'lambda' keyword.
# They can have any number of arguments but only one expression.
# Lambdas are useful for short, simple operations and are often used as arguments
# in higher-order functions like map(), filter(), and sorted().

# Syntax: lambda arguments: expression
# Example:
add = lambda x, y: x + y  # A lambda function that adds two numbers

# Using the lambda function
result = add(3, 5)
print(result)  # Output: 8

# Lambdas are best used for quick tasks, but they are limited to a single expression
# and should be used carefully to maintain code readability.

# Lambdas are quick, one-line anonymous functions defined using the 'lambda' keyword.
# They are often used when a simple function is needed for a short period, without
# the need to formally define it using 'def'.

# Basic Syntax:
# lambda arguments: expression

# Example 1: Simple Addition
# A lambda function that adds two numbers
add = lambda x, y: x + y
print(add(10, 5))  # Output: 15

# Example 2: Using lambda with map()
# Map applies a function to each item in an iterable (like a list).
# In this example, lambda squares each number in the list.
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

# Example 3: Using lambda with filter()
# Filter creates a new list of items for which the function returns True.
# In this example, lambda is used to filter even numbers from a list.
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]

# Example 4: Sorting a List of Tuples
# Lambda is used as the key to sort the list by the second item in each tuple.
pairs = [(1, 2), (3, 1), (5, 0)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(5, 0), (3, 1), (1, 2)]

# Example 5: Using lambda with reduce() (from functools)
# Reduce applies a rolling computation to sequential pairs in a list.
# Here, the lambda function multiplies all elements in the list.
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(product)  # Output: 24

# Example 6: Conditional Expressions in Lambda
# Lambdas can also include conditional logic with a simple if-else.
# This lambda returns the larger of two numbers.
max_value = lambda x, y: x if x > y else y
print(max_value(10, 20))  # Output: 20

# Tips:
# - Lambdas are great for concise, throwaway functions but avoid using them
#   for complex operations that may reduce code readability.
# - Use regular 'def' functions for anything that needs to be reused or is
#   more complex than a single simple expression.




# Creating a list of dictionaries representing Harry Potter characters with their grades
harry_potter_characters = [
    {
        "name": "Harry Potter",
        "house": "Gryffindor",
        "favorite_subject": "Defense Against the Dark Arts",
        "grade": 85
    },
    {
        "name": "Hermione Granger",
        "house": "Gryffindor",
        "favorite_subject": "Arithmancy",
        "grade": 98
    },
    {
        "name": "Ron Weasley",
        "house": "Gryffindor",
        "favorite_subject": "Charms",
        "grade": 74
    },
    {
        "name": "Draco Malfoy",
        "house": "Slytherin",
        "favorite_subject": "Potions",
        "grade": 82
    },
    {
        "name": "Luna Lovegood",
        "house": "Ravenclaw",
        "favorite_subject": "Care of Magical Creatures",
        "grade": 91
    }
]

# Sorting the characters by their grades using lambda
sorted_characters = sorted(harry_potter_characters, key=lambda x: x['grade'])

# Displaying the sorted list of characters
for character in sorted_characters:
    print(character)

# Output will display the characters sorted by their grades in ascending order.
