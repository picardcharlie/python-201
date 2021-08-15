# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_test = [1, 2, 3, 4, 3, 4, 5]

new_set = set(list_test)
print(list(new_set))

test_2 = list_test

for y in list_test:
    if test_2.count(y) > 1:
        test_2.remove(y)

print(test_2)