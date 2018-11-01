# import the random package so that we cna generate random numbers

from random import randint

# choices is an array => a container that can hold multiple items
# arrays are 0-based -> the first item is 0, the second is 1, etc

choices = ["Rock", "Paper", "Scissors"]
player = False

player_lives = 5
computer_lives = 5

# make the computer choose a weapon from choices at random
computer_choice = choices[randint(0, 2)]

# def win or lose funciton
def winorlose(status):
    print("Called inw or lose funciton")
    print("******************************************")
    print("You", status, " ! Would you like to play again?")
    choice = input("Y / N: ")

# reset the lives
    if choice == "Y" or choice == "y":
# change global vaiables
        global player_lives
        global computer_lives
        global player
        global computer

        player_lives = 5
        computer_lives = 5
        player = False
        computer = choices[randint(0,2)]
    elif choice == "N" or choices == "n":
        print("You chose to quit!")
        print("******************************************")
        exit()

# print the choice to the terminal window


print("Computer chooses: ", computer_choice)


while player is False:
    print("====================================")
    print("Player lives: ", player_lives, "/ 5")
    print("Computer lives: ", computer_lives, "/ 5")
    print("====================================")
    # set player to True by making a selection
    print("Choose your weapon!\n")
    player = input("Rock, Paper, Scissors\n")
    print(player, "\n")

    if player == computer_choice:
        print("Tie! You live to shoot another day")
    # check to see if the computer choice beats our choice or not
    elif player == "Rock":
        if computer_choice == "Paper":
            # computer won, crap!
            # #player looses life
            player_lives = player_lives - 1
            print("You lose! Paper covers Rock")
        else:
            # we win! such winning
            computer_lives = computer_lives - 1
            print("You win!", player, "smashes", computer_choice)

    elif player == "Paper":
        if computer_choice == "Scissors":
            player_lives = player_lives - 1
            print("You loose!", computer_choice, "cut", player)
        else:
            computer_lives = computer_lives - 1
            print("You won!", player, "covers", computer_choice)

    elif player == "Scissors":
        if computer_choice == "Rock":
            player_lives = player_lives - 1
            print("You loose!", computer_choice, "smashes", player)
        else:
            computer_lives = computer_lives - 1
            print("You won!", player, "cut", computer_choice)

    elif player == "quit":
        exit()
    else:
        print("Check your spelling... thats not a vaild choice\n")
    if player_lives is 0:
        winorlose("lose")

    if computer_lives is 0:
        winorlose("won")

    player = False
    computer = choices[randint(0, 2)]

