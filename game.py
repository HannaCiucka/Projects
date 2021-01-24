import random

while True:

    ROCK_ACTION = 0
    PAPER_ACTION = 1
    SCISSORS_ACTION = 2

    user_input = input("Choose your weapon (rock[0], paper[1], scissors[2]): ")
    user_choice = int(user_input)


    #possibilities = [0,1,2]
    possibilities = {'rock':0,'paper':1,'scissors':2}

    computers_choice = random.choice(list(possibilities.values()))

    #print(f"\nYou chose {user_choice}, computer chose  {computers_choice}.\n")

    if  computers_choice == user_choice:
        print("It's a tie")
    elif computers_choice == ROCK_ACTION :
        if user_choice == SCISSORS_ACTION :
             print("Computer beat you")
        else:
            print("You win")
    elif computers_choice == PAPER_ACTION :
        if  user_choice == ROCK_ACTION :
            print("Computer beat you")
        else:
            print("You win")

    elif computers_choice == SCISSORS_ACTION:
        if user_choice == PAPER_ACTION:
            print("Computer beat you")
        else:
            print("You win")


    play_again = input("Do you want to play again? (y/n)")
    if play_again.lower() != "y" :
        break
