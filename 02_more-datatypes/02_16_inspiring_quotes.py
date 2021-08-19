# Using f-strings, print out the name, last name,
# and quote of each person in the given dictionary,
# formatted like so:
#
# "The inspiring quote" - Lastname, Firstname

famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]

# It's 7 dictionaries inside of a list, NICE.
# Take the location in the list, get it to print the name and then quote.

# Edit the output in f-strings to show the quote first then then name.
# Figure out how to split a name with a middle letter easy.

for dict in famous_quotes:
    name = dict["full_name"].split()
    quote = dict["quote"]
    print(f'"{quote}" - {" ".join(name[1:])}, {"".join(name[:1])}')