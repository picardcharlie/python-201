# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

# can use .reverse() on a list

with open("words.txt", "r") as textdoc:
    words = textdoc.read().split()
    print(type(words))
    words.reverse()
    reverse = "\n".join(words) #Is programming just googling shit all the time?  Yes.
    output = open("words_reverse.txt", "w")
    output.write(reverse)
    output.close()