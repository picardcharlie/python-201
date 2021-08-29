# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

def division_or(number):
    """
    Determines if a number is devisible by 4 or 7.

    Number is any int.

    Returns True or False.
    """
    result = False
    if number % 4 == 0 or number % 7 == 0:
        result = True

    return result

def division_and(number):
    """
    Determines if number is divisible by 4 AND 7.

    Number is any int.

    Returns True or False.
    """
    result = False
    if number % 4 == 0 and number % 7 == 0:
        result = True

    return result

user_input = int(input("Enter a number between 1 and 1,000,000,000: "))

four_or_seven = division_or(user_input)
four_and_seven = division_and(user_input)

print(f"Is {user_input} devisible by four OR seven? {four_or_seven}")
print(f"Is {user_input} devisible by four AND seven? {four_and_seven}")