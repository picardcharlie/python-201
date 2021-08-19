# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# input hasn't been added and deduce a point.
# If the user gets loses 5 points, quite the program.
# They wil if they manage to create a set that has more than 10 items.

life = 5
all_guess = set()

print("guess unique numbers until you win")

while life >= 1:
    try:
        guess = int(input("What is your guess: "))
    except:
        print("Enter a number...")
        continue

    if guess in all_guess:
        life -= 1
        print(f"You already guessed that, lose one life.  You have {life} left.")

    else:
        all_guess.add(guess)

    if len(all_guess) >= 10:
        print("You win!")
        break

if life <= 1:
    print("You are out of life, you lose!")