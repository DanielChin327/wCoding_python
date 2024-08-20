
#Made a Guess a Number between 1-20
# import random
# while True:
#     number = random.randint(1,20)
#     attempt = 0
#     while True:
#         guess = input("Guess the number from 1 - 20: ")
#         guess = int(guess)
#         if guess == number:
#             attempt += 1
#             print(f"You got it! the number is {number}")
#             print(f"You made {attempt} attempts")
#             quit = input(f"Press any key to continue (type 'quit' to stop)")
#             if quit == "quit":
#                 break
#             else:
#                 number = random.randint(1,20)
#                 attempt = 0
#         elif guess < number:
#             attempt += 1
#             print("Too low...")
#         elif guess > number:
#             attempt += 1
#             print("Too high...")




# 1. String Manipulation

# Exercise 1: Reverse a String
# Write a function `reverse_string(s)` that takes a string `s` and returns the string reversed.

def reverse_string(str):
    return (str[::-1])

# Exercise 2: Count Vowels
# Write a function `count_vowels(s)` that counts the number of vowels (a, e, i, o, u) in a given string `s`.

def count_vowels(str):
    vowels = 'aeiou'
    counter = 0
    for letter in str.lower():
        if letter in vowels:
            counter += 1
    return counter


# Exercise 3: Palindrome Checker
# Write a function `is_palindrome(s)` that checks if the given string `s` is a palindrome (reads the same backward as forward).

def is_palindrom(str):
    if str == str[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

# 2. Conditionals

# Exercise 4: Password Strength Checker
# Write a function `check_password(password)` that checks the strength of a password.
# The password should be at least 8 characters long, contain at least one uppercase letter,
# one lowercase letter, one digit, and one special character (e.g., !@#$%^&*).

# Exercise 5: Grade Calculator
# Write a function `calculate_grade(score)` that returns a grade (A, B, C, D, F)
# based on a score between 0 and 100. Use standard grading scales where A is 90-100,
# B is 80-89, and so on.

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# 3. Loops

# Exercise 6: FizzBuzz
# Write a function `fizz_buzz(n)` that prints numbers from 1 to `n`.
# For multiples of 3, print "Fizz" instead of the number. For multiples of 5, print "Buzz".
# For multiples of both 3 and 5, print "FizzBuzz".

# Exercise 7: Factorial
# Write a function `factorial(n)` that returns the factorial of a given number `n`.

# Exercise 8: Sum of Digits
# Write a function `sum_of_digits(n)` that calculates the sum of all digits of a given number `n`.

# 4. Lists

# Exercise 9: Find the Largest Number
# Write a function `find_largest(nums)` that takes a list of numbers and returns the largest number.

list_nine = [2,4,5,1,3,1,1,4,1,5,6,6,7,8,9,1,2,4,1,3,4,5,20,1,9,3,4,8,1]

def find_largest(array):
    largest_num = array[0]
    for num in array:
        if num > largest_num:
            largest_num = num
    return largest_num


# Exercise 10: Remove Duplicates
# Write a function `remove_duplicates(lst)` that takes a list and returns a new list with duplicate elements removed.

def remove_duplicates(array):
    result = []
    for num in array:
        if num not in result:
            result.append(num)
    return result


# Exercise 11: Sum of List Elements
# Write a function `sum_list(lst)` that takes a list of numbers and returns the sum of all elements.

def sum_list(list):
    sum = 0
    for num in list:
        sum += num
    return sum




# Exercise 12: Sort a List
# Write a function `sort_list(lst)` that sorts a list of numbers in ascending order without using the built-in `sort` method.


# 5. Dictionaries

# Exercise 13: Count Word Frequency
# Write a function `word_frequency(sentence)` that takes a string sentence and returns a dictionary
# with each word as a key and its frequency as the value.





# Exercise 14: Student Grades
# Write a function `student_grades(students)` that takes a dictionary of student names as keys
# and their scores as values, and returns a new dictionary with student names and their corresponding grades (A, B, C, D, F).

# Exercise 15: Inventory Management
# Write a function `update_inventory(inventory, item, quantity)` that updates a dictionary `inventory`
# with the item and its quantity. If the item already exists, update its quantity;
# otherwise, add the item to the dictionary.

# 6. Combining Concepts

# Exercise 16: Password Generator
# Write a function `generate_password(length)` that generates a random password of a given `length`.
# The password should contain at least one uppercase letter, one lowercase letter, one digit, and one special character.

# Exercise 17: Caesar Cipher
# Write a function `caesar_cipher(text, shift)` that encrypts a given `text` using the Caesar cipher technique
# by shifting each letter by the specified `shift` value.

# Exercise 18: Simple Calculator
# Write a function `calculator(a, b, operation)` that performs basic arithmetic operations (`+`, `-`, `*`, `/`)
# on two numbers `a` and `b` based on the operation provided.
