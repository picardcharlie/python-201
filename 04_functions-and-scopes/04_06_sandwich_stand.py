# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(bread = "Sourdough", *args):
    sandwich = str(bread) + " "

    for toppings in args:
        sandwich += toppings + " "

    sandwich += str(bread)

    return sandwich

items = ["cheese", "beef"]
print(make_sandwich("White bread", *items))