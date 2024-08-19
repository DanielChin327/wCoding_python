# name1 = input("What is first name: ")
# name2 = input("What is middle name: ")
# name3 = input("What is last name: ")

# fullname = name1 + " " + name2 + " " + name3

# Method One

# Determine the positions of each name within the fullname string
# length_name1 = len(name1)
# length_name2 = len(name2)

# Extract and print each part by slicing
# print(fullname[:length_name1])  # First name
# print(fullname[length_name1 + 1:length_name1 + 1 + length_name2])  # Middle name
# print(fullname[length_name1 + 1 + length_name2 + 1:])  # Last name

# Split Method
# fullname_list = fullname.split(' ')

# print(fullname_list[0])
# print(fullname_list[1])
# print(fullname_list[2])

# Exercise 1: Reverse a String
# Write a program that takes a string as input and prints it in reverse order.
exercise_one = 'reversed'
exercise_one_reversed = exercise_one[::-1]
# print(exercise_one_reversed)

# Exercise 2: Count Vowels and Consonants
# Write a program that counts the number of vowels and consonants in a given string.
# ex_two = "check the number of vowels and consonents in this message"

# vowels ="aeiouAEIOU"

# vowel_count = 0
# consonant_count = 0

# for letters in ex_two:
#     if letters.isalpha(): #checks if character is an alphabet.
#         if letters in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1

# print("Vowel Count: ", vowel_count," Consonant Count: ", consonant_count)



# Exercise 3: Check Palindrome
# Write a program that checks whether a given string is a palindrome.

# def is_palindrome(text):
#     text = text.lower()
#     return text == text[::-1] #text[::-1] reverses text


# if is_palindrome(text):
#     print("yes")
# else:
#     print("No")
# Exercise 4: Find the Longest Word
# Write a program that takes a string of words and returns the longest word.

def longest_word(string):
    array = string.split(" ")
    result = array[0]
    for element in array:
        if len(element) > len(result):
            result = element
    return result

print (longest_word("What is the longest word"))

# Exercise 5: Replace a Substring
# Write a program that replaces all occurrences of a specified substring with another substring.

# text = input("Enter the original text: ")
# to_replace = input("Enter the substring to replace: ")
# replacement = input("Enter the replacement substring: ")

# new_text = text.replace(to_replace, replacement)
# print(new_text)

# Exercise 6: Capitalize First and Last Letters of Each Word
# Write a program that capitalizes the first and last letters of every word in a given string.

# def capitalize(string):
#     words = string.split()
#     words_capitalized = []

#     for word in words:
#         if len(word) > 1:
#             words_capitalized = word[0].upper() + word[1:-1] + word[-1].upper()
#         else:
#             words_capitalized = word.upper()
#         words_capitalized.append(words_capitalized)
#     return ''.join(words_capitalized)


# Exercise 7: Find All Occurrences of a Substring
# Write a program that finds all occurrences of a substring in a string and returns their positions.




# Exercise 8: Remove Duplicates
# Write a program that removes all duplicate characters from a string.

# Exercise 9: Swap Case
# Write a program that swaps the case of all letters in a string (lowercase to uppercase and vice versa).

# Exercise 10: Count Words in a String
# Write a program that counts the number of words in a given string.

# Exercise 11: Check for Anagrams
# Write a program that checks whether two given strings are anagrams.

# Exercise 12: Print a String in a Zigzag Pattern
# Write a program that prints a string in a zigzag pattern.


word = 'word One'
word2 = 'word two'
word3 = 'word three'

list = []

list.append(word)
list.append(word2)

print(list)
