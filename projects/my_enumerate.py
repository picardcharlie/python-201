# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(list_input: list, starting_point = 0):# add your arguments
      """
      Takes a list and adds an index number to each item in the list.

      Accepts the list that needs indexing and what number to start at.  Default is zero.

      Prints out a list of tulips with the (index value, item).
      """

      output_list = []
      start = starting_point

      for item in list_input:
            output_list += tuple([start, item])
            start += 1

      return output_list

city = ["Minneapolis", "Taipei", "Onterio"]

print(my_enumerate(city))
