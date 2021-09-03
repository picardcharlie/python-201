# Take a number from the user, 0-2 to represent their hand. Generate one for computer.
# Use a function called "get_hand" to get the string of what was called for both players.
# Use function "determine_winner" to, you know...
# Print both players hands, print winner.

import random
# random.randint(0, 2)

def get_hand(hand: int):
    """ Get user input and convert it to a string.

    Takes an int representing rock, paper, scissors.

    Return a string with the right hand.
    """
    call = ""

    if hand == 0:
        call = "rock"
    elif hand == 1:
        call = "paper"
    elif hand == 2:
        call = "scissor"

    return call

def determine_winner(playerhand: int, robothand: int):
    """ Checks to see who won in rock, paper, scissor.

    Takes in the player's hand and the computer's hand.

    Returns the winner as a string.
    """

    winner = ""

    # 0 = rock, 1 = paper, 2 = scissor
    if playerhand == robothand:
        winner = "no one, it's a tie"
    elif playerhand == 0 and robothand == 1:
        winner = "the computer"
    elif playerhand == 0 and robothand == 2:
        winner = "the player"
    elif playerhand == 1 and robothand == 0:
        winner = "the player"
    elif playerhand == 1 and robothand == 2:
        winner = "the computer"
    elif playerhand == 2 and robothand == 0:
        winner = "the computer"
    elif playerhand == 2 and robothand == 1:
        winner = "the player"

    return winner

# get user input
print("Rock = 0, Paper = 1, Scissor = 2")
player = int(input("What do you throw: "))

#generate computer hand
computer = random.randint(0, 2)

#fstring it real hard with functions
print(f"Player threw {get_hand(player)}, the computer threw {get_hand(computer)}.  The winner is {determine_winner(player, computer)}!")