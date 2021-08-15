# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

input_string = input("Enter a string that has at least two of the same word: ")

string_list = input_string.split()

biggest = [None, 0]

for y in string_list:
    if string_list.count(y) > 1 and string_list.count(y) > biggest[1]:
        biggest = [y, string_list.count(y)]

print(biggest[0])