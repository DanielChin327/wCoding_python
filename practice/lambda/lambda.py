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
