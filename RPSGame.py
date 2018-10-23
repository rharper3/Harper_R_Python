# import the random package so that we cna generate random numbers

from random import randint

# choices is an array => a container that can hold multiple items
# arrays are 0-based -> the first item is 0, the second is 1, etc

choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer choose a weapon from choices at random

computer_choice = choices[randint(0, 2)]

# print the choice to the terminal window

print("Computer chooses: ", computer_choice)

while player is False:
    # set player to True by making a selection
    print("Choose your weapon!")
    player = input("Rock, Paper, Scissors?")

    print(player, "\n")

    if player == computer_choice:
        print("Tie! You live to shoot another day")
    # check to see if the computer choice beats our choice or not
    elif player == "Rock":
        if computer_choice == "Paper":
            # computer won, crap!
            print("You lose! Paper covers Rock")
        else:
            # we win! such winning
            print("You win!", player, "smashes", computer_choice)

    elif player == "Paper":
        if computer_choice == "Scissors":
            print("You loose!", computer_choice, "cut", player)
        else:
            print("You won!", player, "covers", computer_choice)

    elif player == "Scissors":
        if computer_choice == "Rock":
            print("You loose!", computer_choice, "smashes", player)
        else:
            print("You won!", player, "cut", computer_choice)

    elif player == "quit":
        exit()
    else:
        print("Check your sppelling... thats not a vaild choice\n")
