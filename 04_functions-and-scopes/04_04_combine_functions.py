# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(name):
    return print(f"Hello {name}!")

def write_letter(name, text):
    greet(name)
    print(f"{text}")
    print(f"Well I must be going now {name}, I hope to hear from you soon. \n Love, \n Charlie")
    return

write_letter("duffinz", "I love eating cheese") # Common Irish name.