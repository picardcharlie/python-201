# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.


def write_letter(name, text):
    print(f"Hello {name}, it's been too long!")
    print(f"{text}")
    print(f"Well I must be going now {name}, I hope to hear from you soon. \n Love, \n Charlie")
    return


write_letter("Carl", "I gotta poop.") #Some late night comedy, nbd.  Watch my netflix special coming September 32nd!