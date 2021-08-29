# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(*args):
  """
  Finds the max, min, average and sum of all numbers.

  Accepts a list of ints.

  Returns everthing as an int or float.
  """
  # define the function here
  maximum = max(args)
  minimum = min(args)
  average = sum(args) / len(args)
  total_sum = sum(args)
  return maximum, minimum, average, total_sum

# call the function below here
print(stats(*example_list))