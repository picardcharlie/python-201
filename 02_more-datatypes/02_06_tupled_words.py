# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

string = input("Enter a sentence: ")

list_string = string.split()

final_list = [tuple(y) for y in list_string]

print(final_list)