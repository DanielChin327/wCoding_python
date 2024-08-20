string_one = "This is a message to the world"
string_two = "Hello"


split_string = string_one.split()[0]

# string_one.split() -> ['This', 'is', 'a', 'message', 'to', 'the', 'world'] -> list
# string_one.split()[0] -> This -> str
# string_one.split()[0][0] ->T -> str


# combine the two message and then swap the first two letters in the words.
# Messages
message_one = "Hello"
message_two = "World"

# Combine the messages into one string
combined_message = message_one + " " + message_two

# Split the combined message into words
words = combined_message.split()

# Swap the first two letters of each word
# Form the new words by slicing and combining
new_word_one = message_two[:2] + message_one[2:]
new_word_two = message_one[:2] + message_two[2:]

# Join the new words into the final result
result = new_word_one + " " + new_word_two

print(result)
