from msilib.schema import Error
import time
from human import Human
from ai import Ai
from player import Player


def display_welcome():
    print("Welcome to Rock Paper Scissors Lizard Spock")
    print("")
    time.sleep(.5)
    print("Best of 3 will be the winner")
    print("Use the number keys to choose your attack")
    print("")
    print("")
    time.sleep(.5)
    print("Rock crushes Scissors")
    time.sleep(.5)
    print("Scissors cuts Paper")
    time.sleep(.5)
    print("Paper covers Rock")
    time.sleep(.5)
    print("Rock crushes Lizard")
    time.sleep(.5)
    print("Lizard poisons Spock")
    time.sleep(.5)
    print("Spock smashes Scissors")
    time.sleep(.5)
    print("Scissors decapitates Lizard")
    time.sleep(.5)
    print("Lizard eats Paper")
    time.sleep(.5)
    print("Paper disproves Spock")
    time.sleep(.5)
    print("Spock vaporizes Rock")
    print("")
    print("")

def player_count():
    players = (input("How many players? 1, 2, or 3? "))
    if players == "1":
        player_one = Human("Player One")
        player_two = Ai("Player Two")
    elif players == "2":
        player_one = Human("Player One")
        player_two = Human("Player Two")
    elif players == "3":
        player_one = Ai("Player One")
        player_two = Ai("Player Two")
    else:
        print(Error)
        

def play_game():
    while player_one.score < 2 and player_two.score > 2:
        if player_one.chosen_gesture == player_two.chosen_gesture:
            print(f"Both players selected {player_one.chosen_gesture}. It's a tie!")
        elif player_one.chosen_gesture == "Rock":
            if player_two.chosen_gesture == "Scissors":
                player_one.score =+ 1
                print("Rock crushes Scissors! You win!")
            elif player_two.chosen_gesture == "Lizard":
                player_one.score =+ 1
                print("Rock crushes Lizard! You win!")
            elif player_two.chosen_gesture == "Paper":
                player_two.score =+ 1
                print("Paper covers Rock! You lose!")
            elif player_two.chosen_gesture == "Spock":
                player_two.score =+ 1
                print("Spock vaporizes Rock! You lose!")
        elif player_one.chosen_gesture == "Paper":
            if player_two.chosen_gesture == "Scissors":
                player_one.score =+ 1
                print("Scissors cuts Paper! You win!")
            elif player_two.chosen_gesture == "Spock":
                player_one.score =+ 1
                print("Paper disproves Spock! You win!")
            elif player_two.chosen_gesture == "Scissors":
                player_two.score =+ 1
                print("Scissors cuts Paper! You lose!")
            elif player_two.chosen_gesture == "Lizard":
                player_two.score =+ 1
                print("Lizard eats Paper! You lose!")
        elif player_one.chosen_gesture == "Scissors":
            if player_two.chosen_gesture == "Paper":
                player_one.score =+ 1
                print("Scissors cuts Paper! You win!")
            elif player_two.chosen_gesture == "Lizard":
                player_one.score =+ 1
                print("Scissors decapitates Lizard. You win!")
            elif player_two.chosen_gesture == "Rock":
                player_two.score =+ 1
                print("Rock crushes Scissors! You lose!")
            elif player_two.chosen_gesture == "Spock":
                player_two.score =+ 1
                print("Spock smashes Scissors! You lose!")
        elif player_one.chosen_gesture == "Lizard":
            if player_two.chosen_gesture == "Paper":
                player_one.score =+ 1
                print("Lizard eats Paper! You win!")
            elif player_two.chosen_gesture == "Spock":
                player_one.score =+ 1
                print("Lizard poisons Spock. You win!")
            elif player_two.chosen_gesture == "Rock":
                player_two.score =+ 1
                print("Rock crushes Lizard! You lose!")
            elif player_two.chosen_gesture == "Scissors":
                player_two.score =+ 1
                print("Scissors decapitates Lizard! You lose!")
        elif player_one.chosen_gesture == "Spock":
            if player_two.chosen_gesture == "Scissors":
                player_one.score =+ 1
                print("Spock smashes Scissors! You win!")
            elif player_two.chosen_gesture == "Rock":
                player_one.score =+ 1
                print("Spock vaporizes Rock. You win!")
            elif player_two.chosen_gesture == "Lizard":
                player_two.score =+ 1
                print("Lizard poisons Spock! You lose!")
            elif player_two.chosen_gesture == "Paper":
                player_two.score =+ 1
                print("Paper disproves Spock! You lose!")


def declare_winner():
        if player_one.score == 2:
                print("Player One is the winner!")
        elif player_two.score == 2:
                print("Player Two is the winner!")