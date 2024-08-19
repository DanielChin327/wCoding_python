print("Hello, World!")

name = "Alice"
age = 25
height = 5.5

integer_var = 10       # int
float_var = 10.5       # float
string_var = "Hello"   # str
bool_var = True        # bool

sum = 5 + 3
difference = 5 - 3
product = 5 * 3
quotient = 5 / 3
remainder = 5 % 3
power = 5 ** 3


# This is a comment

"""
This is a
multi-line comment
"""

if age >= 18:
    print("You are an adult.")
elif age > 12:
    print("You are a teenager.")
else:
    print("You are a child.")


# for loop: Iterate over a sequence.
for i in range(5):
    print(i)  # Prints 0 to 4

max_number = input("Give a number: ")
max_number = int(max_number)

for i in range(1, max_number):
    if i % 3 == 0 and i % 5 == 0:
        print ('FizzBuzz')
    elif i % 3 == 0:
        print ('Fizz')
    elif i % 5 == 0:
        print ('Buzz')
    else:
        print(i)


# while loop: Repeat as long as a condition is true.
count = 5
while count < 5:
    print(count)
    count += 1  # Increment count by 1

# Functions Defining a function: Use def keyword.
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Calls the function with "Alice"

fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # Outputs: apple

fruits.append("orange")

fruits.remove("banana")


# Dictionares Creating a dictionary: Collection of key-value pairs.
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

person["email"] = "alice@example.com"
print(person["name"])  # Outputs: Alice
