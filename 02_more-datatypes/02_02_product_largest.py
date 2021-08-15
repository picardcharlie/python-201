# Take in 10 numbers from the user. Place the numbers in a list.
# You can also use the provided random `randlist` list
# to simulate user input.
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist

print(randlist)

largest = 0
product = 0

for y in randlist:
    if y > largest:
        largest = y

    product += y

print(f"The largest number in the list is {largest} and the product of it is {product}")