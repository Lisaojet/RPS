
import random

input("Welcome to Rock-Paper-Scisssors Game! Press enter to continue")
print()
print("The rules of the game is as follows: \n"
      "Rock beats Scissors \n"
      "Paper beats Rock \n"
      "Scissors beats Paper \n")


while True:
    possible_options = ["rock", "paper", "scissors"]

    computer = random.choice(possible_options)
    player = None

    while player not in possible_options:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print(f"\Player {(player)}, vs CPU {(computer)}.")
        print("It is a tie! Play again!")

    elif player == "rock":
        if computer == "paper":
            print(f"\Player {(player)}, vs CPU {(computer)}.")
            print("Paper beats Rock")
            print("Oops! You lose!1")
            break
        if computer == "scissors":
            print(f"\Player {(player)}, vs CPU {(computer)}.")
            print("Rock beats Scissors")
            print("Congratulations! You win!")
            break

    elif player == "scissors":
        if computer == "rock":
            print(f"\Player {(player)}, vs CPU {(computer)}.")
            print("Rock beats Scissors")
            print("Oops! You lose!")
            break
        if computer == "paper":
            print(f"\Player {(player)}, vs CPU {(computer)}.")
            print("Scissors beats Paper")
            print("Congratulations! You win!")
            break

    elif player == "paper":
        if computer == "scissors":
            print(f"\Player {(player)}, vs CPU {(computer)}.")
            print("Scissors beats Paper")
            print("Oops! You lose!")
            break
        if computer == "rock":
            print(f"\Player {(player)}, vs CPU {(computer)}.")
            print("Paper beats Rock")
            print("Congratulations! You win!")
            break

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")
