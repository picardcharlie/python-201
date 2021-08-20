# Add the code for the file counter script that you wrote in the course.
# Collect and count how many of each file type are in cwd.
# Put all data into a dictionary and print it out. can use pprint() to display it "prettier"
# If more than five of one type, move them all into their own folder.

import pathlib

inventory = {"directory": 0}

for file in pathlib.path().cwd().interdir():
    # Check if it's a file.
    if file.is_dir() == True:
        inventory["directory"] += 1

    # Check if the extension is in the dictionary, if not add it.
    if file.suffix() in inventory.keys():
        inventory[file.suffix()] += 1
    elif file.suffix() not in inventory.keys():
        inventory[file.suffix()] = 1

for ext in inventory:
    print(f"There are {inventory[ext].values()} {inventory[ext].keys()}.")

file_sort = input("Would you like to do a basic sort of your files (Y/N)? ")

if file_sort.lower() == "y" or file_sort.lower() == "yes":
    # Go through the dictionary, if there is more than five of a file type make a folder and put them in it.
    for type in inventory:
        if type == "directory":
            pass
        elif inventory[type] >= 5:
            type.mkdir(exist_ok = True) #Made a new directory with the file type for a name.
            for filetype in pathlib.Path().cwd().interdir():
                #Check to see if it's the correct file type and not another directory.
                if filetype.suffix() == type and filetype.is_dir() == False:
                    new_path_move = type.joinpath(filetype.name)
                    filetype.replace(new_path_move)

#
