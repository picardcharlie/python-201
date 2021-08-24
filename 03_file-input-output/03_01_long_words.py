# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

with open("words.txt", "r") as textdoc:
    wordss = textdoc.read().split()   #Kinda of ugly, but is this standard practice?

    for entree in wordss:
        if len(entree) >= 20:
            print(entree)
