
import random

input("Welcome to Rock-Paper-Scisssors Game! \n" 
      "Press enter to continue")
print()
print("The rules of the game is as follows: \n"
      "Rock beats Scissors \n"
      "Paper beats Rock \n"
      "Scissors beats Paper \n")

options_list = ["R", "P", "S"]
options_dict = {"R": "Rock", "P": "Paper", "S": "Scissors"}

while True:
    possible_options = ["R", "P", "S"]

    computer = random.choice(options_list)
    player = None

    while player not in options_list:
        player = input("Enter R for Rock, P for Paper, or S for Scissors?: ").upper()

    if player == computer:
        print(f"Player ({options_dict[player]}) vs CPU ({options_dict[computer]})")
        print("It is a tie! Play again!")
        continue

    elif player == "R":
        if computer == "P":
            print(f"Player ({options_dict[player]}) vs CPU ({options_dict[computer]})")
            print("Paper beats Rock")
            print("Oops! You lose!")
            break
        if computer == "S":
            print(f"Player ({options_dict[player]}) vs CPU ({options_dict[computer]})")
            print("Rock beats Scissors")
            print("Congratulations! You win!")
            break

    elif player == "S":
        if computer == "R":
            print(f"Player ({options_dict[player]}) vs CPU ({options_dict[computer]})")
            print("Rock beats Scissors")
            print("Oops! You lose!")
            break
        if computer == "P":
            print(f"Player ({options_dict[player]}) vs CPU ({options_dict[computer]})")
            print("Scissors beats Paper")
            print("Congratulations! You win!")
            break

    elif player == "P":
        if computer == "S":
            print(f"Player ({options_dict[player]}) vs CPU ({options_dict[computer]})")
            print("Scissors beats Paper")
            print("Oops! You lose!")
            break
        if computer == "R":
            print(f"Player ({options_dict[player]}) vs CPU ({options_dict[computer]})")
            print("Paper beats Rock")
            print("Congratulations! You win!")
            break

    else:
          print("\nInvalid input! Please try again.")
          continue

print("Bye!")

