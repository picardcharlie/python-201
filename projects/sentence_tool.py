# Write a tool that counts different variables inside of a sentence.
# Keep track of, lower case letters, uppercase, number of punctuations, total number of characters.
# Store values in a dictionary.
# Note: ignore spaces.

import string #Wanted to use string.punctuation for ease.

new_sent = input("Enter a sentence: ")

sent_values = {"lowercase": 0, "uppercase": 0, "punct": 0, "characters": 0}

for char in new_sent:
    if char.islower() == True and char.isspace() == False:
        sent_values["lowercase"] += 1
    elif char.isupper() == True and char.isspace() == False:
        sent_values["uppercase"] += 1
    elif char in string.punctuation:
        sent_values["punct"] += 1

    if char.isspace() == False:
        sent_values["characters"] +=1

print(f"Total number of uppercase: {sent_values['uppercase']}")
print(f"Total number of lowercase: {sent_values['lowercase']}")
print(f"Total number of punctuations: {sent_values['punct']}")
print(f"Total number of characters: {sent_values['characters']}")