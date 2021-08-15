# Write code that creates a list of all unique values in a list.
# For example:
# use .count() you boomer -Charlie
list_test = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

unique = []

for dex in list_test:
    if list_test.count(dex) == 1:
        unique.append(dex)

print(unique)

# I did this so backwards, keep trying to remove from a list instead of just adding to one.