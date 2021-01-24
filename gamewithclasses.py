import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ",".join(choices)
    #user_input = input("Enter a choice (rock[0], paper[0], scissors[1])")
    selection = int(input(f"Enter a choice({choices_str}): "))
    action = Action(selection)
    return action

def get_computers_selection():
    selection = random.randint(0,len(Action) - 1)
    action = Action(selection)
    return action

def determine_winner(user_action, computers_action):
    if  user_action == computers_action:
        print (f"Both players selected {user_action.name}.")
    elif user_action == Action.Rock:
        if computers_action == Action.Scissors:
            print("Rock beats scissors, you win !")
        else:
            print ("You lose")
    elif user_action == Action.Paper:
        if computers_action == Action.Rock:
            print("Paper covers rock. You win !")
        else:
            print ("You lose")
    elif user_action == Action.Scissors:
        if computers_action == Action.Paper:
            print ("Scissors cuts the paper, you win !")
        else:
            print ("You lose")

while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0,{len(Action) - 1}]"
        print(f"Invalid number. Choose something from range 0-2.")
        continue
    computers_action = get_computers_selection()
    determine_winner(user_action, computers_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
