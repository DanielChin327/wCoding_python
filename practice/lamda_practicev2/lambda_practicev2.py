# 1. Write a function that will find the sum of a series of repeating digits equal in number to n
	# e.g. 3 + 33 + 333 + 3333 + 33333 ... n times
	# The function should take in two arguments, n and the digit to repeat OR you can write 2 seperate functions

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

	##### CHALLENGE ##### allow user imput for the number of rows they'd like to print out for the pattern above

# 3. Write a SINGLE function that accepts 2 numbers, return the sum, difference, product and quotient of the two numbers at 4 seperate variables.

# 4. Write a function that takes 2 integer arguments and returns a list of every even number between them
	# e.g. arguments = 3 and 17, return [4, 6, 8, 10, 12, 14, 16]

# 5. Write a function that iterates through a list and returns the largest number in that list. DON'T USE THE MAX() FUNCTION for practice

# 6. Write a function that accepts user input and determines if the string OR number is a palindrome
	# a palindrome is a word or phrase that reads the same backwards and forwards
	# racecar, madam, 123454321, 10101, etc.
