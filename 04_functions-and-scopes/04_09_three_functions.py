# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

def plus(number):
    number += number
    return number

def minus(number):
    number -= number
    return number

def multiply(number):
    number *= number
    return number

def exponential(number):
    number = number ** number
    return number

print(exponential(multiply(plus(2))))