# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

# Write your code below here
if len(randlist) % 2 != 0:
    randlist.append(0)
print(randlist)

list_sort = randlist
list_sort.sort()
print(list_sort)

tuple_list = []
for y in range(len(list_sort)):
    if y == 0:
        tuple_list.append(tuple(list_sort[y:y+2]))

    if y % 2 == 0 and y != 0:
        tuple_list.append(tuple(list_sort[y:y+2]))

print(tuple_list)


