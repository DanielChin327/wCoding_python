string_one = "This is a message to the world"
string_two = "Hello"


split_string = string_one.split()[0]

# string_one.split() -> ['This', 'is', 'a', 'message', 'to', 'the', 'world'] -> list
# string_one.split()[0] -> This -> str
# string_one.split()[0][0] ->T -> str


# combine the two message and then swap the first two letters in the words.
message_one = "Hello"
message_two = "World"


combined = message_one + " " + message_two

split_combined = combined.split()[1][0] + combined.split()[0][2]

print (combined.split()[0][2])
# print (split_combined)
