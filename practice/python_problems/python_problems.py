# 1. Write a function that will find the sum of a series of repeating digits equal in number to n
	# e.g. 3 + 33 + 333 + 3333 + 33333 ... n times
	# The function should take in two arguments, n and the digit to repeat OR you can write 2 seperate functions

import math

def sum_num(n, digit):
    digit_str = str(digit)
    num_str = ''
    counter = 1
    while counter <= n:
        num_str += digit_str
        counter += 1
    number_list = [int(char) for char in num_str]
    total = sum(number_list)
    return total

print(sum_num(3, 2))
# 2. Print out the following pattern
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

def triangle():
    counter = 1
    star = "*"
    while counter <= 5:
        print(star)
        star += " *"
        counter += 1
    while counter >= 0:
        counter -= 1
        print(star)
        star = star[:-1]



	##### CHALLENGE ##### allow user imput for the number of rows they'd like to print out for the pattern above

# 3. Write a SINGLE function that accepts 2 numbers, return the sum, difference, product and quotient of the two numbers at 4 seperate variables.

def calculate(num1, num2):
    sum = num1 + num2
    diff = num1 - num2
    product = num1 * num2
    quotient = num1/num2
    return sum, diff, product, quotient


# 4. Write a function that takes 2 integer arguments and returns a list of every even number between them
	# e.g. arguments = 3 and 17, return [4, 6, 8, 10, 12, 14, 16]

def evens(num1, num2):
    list = []
    start = num1
    end = num2
    while start <= end:
        if start % 2 == 0:
            list.append(start)
        start +=1
    return list



# 5. Write a function that iterates through a list and returns the largest number in that list. DON'T USE THE MAX() FUNCTION for practice

def max_num(list):
    result = list[0]
    for num in list:
        if result < num:
            result = num
    return result


# 6. Write a function that accepts user input and determines if the string OR number is a palindrome
	# a palindrome is a word or phrase that reads the same backwards and forwards
	# racecar, madam, 123454321, 10101, etc.


def palindrome_check():
    message = input("Check if message is palindrome:   ")
    message = message.lower()
    message_list = list(message)
    for index in range(math.floor(len(message_list) / 2)):
        if message_list[index] != message_list[-(index + 1)]:
            return "Not Palindrome."

    return "It is Palindrome."


print(palindrome_check())


# PYTHON PRACTICE PROBLEMS

# 1. Print "Hello, World!"
# Write a program that outputs "Hello, World!" to the console.

# 2. Variables and Basic Arithmetic
# Create two variables, a and b. Assign them values 10 and 20.
# Print their sum, difference, product, and division.

# 3. String Manipulation
# Take a string variable with the value "Python Programming".
# Print the string in uppercase, lowercase, and reverse order.

# 4. Even or Odd
# Write a program that checks if a given number is even or odd.
# Example: If the input is 4, print "Even".

# 5. List Operations
# Create a list of 5 numbers.
# Perform the following:
# - Append a new number to the list.
# - Remove the second element.
# - Sort the list in ascending order.
# - Print the updated list.

# 6. FizzBuzz
# Write a program that prints numbers from 1 to 50.
# But for multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz".
# For numbers which are multiples of both 3 and 5, print "FizzBuzz".

# 7. Palindrome Checker
# Write a function that takes a string and returns True if it is a palindrome, False otherwise.
# A palindrome is a word that reads the same backward as forward (e.g., "radar").

# 8. Dictionary Operations
# Create a dictionary with keys as fruits and values as their prices (e.g., {"apple": 1.2, "banana": 0.5}).
# Perform the following:
# - Add a new fruit to the dictionary.
# - Update the price of an existing fruit.
# - Delete a fruit from the dictionary.
# - Print the final dictionary.

# 9. Factorial Function
# Write a function that calculates the factorial of a number.
# Example: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120

# 10. Prime Number Checker
# Write a function that checks if a number is prime.
# A number is prime if it has no divisors other than 1 and itself.

# 11. File Handling
# Write a program that creates a text file named "example.txt".
# Write the text "Hello, file handling!" into the file.
# Read the content of the file and print it to the console.

# 12. Rock, Paper, Scissors
# Create a simple rock-paper-scissors game where the user plays against the computer.
# The computer's choice should be random.

# 13. Simple Calculator
# Write a program that performs addition, subtraction, multiplication, and division.
# Take two numbers and the operation as input from the user.

# 14. Fibonacci Sequence
# Write a function that prints the first N numbers in the Fibonacci sequence.
# Example: For N=5, the output should be 0, 1, 1, 2, 3.

# 15. Guess the Number
# Create a program where the user guesses a randomly generated number between 1 and 100.
# Provide hints like "Too high!" or "Too low!" after each guess.

# 16. Find Maximum in a List
# Write a function that takes a list of numbers and returns the maximum value.

# 17. Counting Characters
# Write a program that counts the number of vowels and consonants in a given string.

# 18. Password Generator
# Create a program that generates a random password of a specified length.
# The password should include uppercase, lowercase, digits, and special characters.

# 19. Sorting a List of Tuples
# Given a list of tuples, sort the list based on the second element of each tuple.
# Example: [(1, 3), (4, 2), (2, 5)] -> [(4, 2), (1, 3), (2, 5)]

# 20. Leap Year Checker
# Write a program that checks if a given year is a leap year.

# 21. Count Words in a File
# Write a program that reads a text file and counts the number of words in it.

# 22. Hangman Game
# Create a simple hangman game where the user guesses letters to figure out a word.
# Display the partially guessed word and remaining attempts after each guess.

# 23. Shopping Cart System
# Create a simple shopping cart system where users can add items, remove items, and view the total cost.

# 24. Reverse Words in a Sentence
# Write a program that reverses the order of words in a given sentence.
# Example: "Hello World" -> "World Hello"

# 25. JSON Handling
# Create a program that writes a dictionary to a JSON file and then reads it back.
# Example: Save {"name": "John", "age": 30} to a JSON file.

# 26. Temperature Converter
# Write a program to convert temperatures between Celsius and Fahrenheit.

# 27. Find Common Elements in Two Lists
# Write a function that finds common elements between two lists.
# Example: [1, 2, 3], [2, 3, 4] -> [2, 3]

# 28. Simple Bank System
# Create a class `BankAccount` with methods for deposit, withdrawal, and balance inquiry.

# 29. Tic-Tac-Toe Game
# Create a simple text-based Tic-Tac-Toe game for two players.

# 30. Web Scraper
# Write a program using the `requests` and `BeautifulSoup` libraries to scrape the title of a webpage.
# (You may need to install these libraries first.)

# Feel free to expand, modify, or improve these exercises as you work through them.
