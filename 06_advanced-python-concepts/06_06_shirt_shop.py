# Using a list comprehension, create a *cartesian product* (google this!)
# of the given lists. Then open up your online shop ;)

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

# cartesian is a table made by multiplying all of one set against each element in another.

cart = [[x] + sizes for x in colors]
print(cart)