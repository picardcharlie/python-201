# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

with open("words.txt", "r") as textdoc:
    all_the_words = textdoc.read().split() #Throw it all in a list

    # Puts all the words into a dictionary with their length as their value.
    words_dict = {}
    for word in all_the_words:
        words_dict[word] = len(word)

    # list of all the values in the dictionary.  min(), max(), len() for total entrees
    value_list = list(words_dict.values())

    #list of all the keys in the dictionary. Can print all the keys using the position from the values list.
    key_list = list(words_dict.keys())

    # Make a list, add the shortest word length and then search key list for that length from value list location.
    shortest = []
    shortest.append(min(value_list))

    # dump all the words that are the shortest length into the list.
    for location in range(len(value_list)):
        if value_list[location] == shortest[0]:
            shortest.append(key_list[location])

    print(f"The shortest word length is {shortest[0]}, these are the words:", end = "")

    x = 0
    for word in shortest[1:]:
        if x % 20 == 0:
            print("")
        print(word, end = "  ")
        x += 1
    print("\n")

    longest = []
    longest.append(max(value_list))
    for spot in range(len(value_list)):
        if value_list[spot] == longest[0]:
            longest.append(key_list[spot])

    print(f"The longest word length is {longest[0]}, these are the words:", end = '')

    y = 0
    for word in longest[1:]:
        if y % 4 == 0:
            print("")
        print(word, end = "  ")
        y += 1

    print("\n")
    print(f"The total number of words in the file is: {len(value_list)}")