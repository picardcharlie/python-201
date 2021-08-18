# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}
dict = {}

#dict.update(dict_1)
#dict.update(dict_2)

for y in dict_1.keys():
    if y in dict_2:
        dict[y] = dict_1[y] + dict_2[y]
    elif y not in dict_2:
        dict[y] = dict_1[y]

for x in dict_2.keys():
            if x not in dict_1:
                dict[x] = dict_2[x]
print(dict)