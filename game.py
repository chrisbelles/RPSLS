# Rock crushes Scissors   
# Scissors cuts Paper  
# Paper covers Rock  
# Rock crushes Lizard  
# Lizard poisons Spock  
# Spock smashes Scissors  
# Scissors decapitates Lizard  
# Lizard eats Paper  
# Paper disproves Spock  
# Spock vaporizes Rock  

# List = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

import time
from human import Human
from ai import Ai


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


if human_gesture == ai_gesture:
    print(f"Both players selected {human_gesture}. It's a tie!")
elif human_gesture == "Rock":
    if ai_gesture == "Scissors":
        print("Rock crushes Scissors! You win!")
    elif ai_gesture == "Lizard":
        print("Rock crushes Lizard! You win!")
    elif ai_gesture == "Paper":
        print("Paper covers Rock! You lose!")
    elif ai_gesture == "Spock":
        print("Spock vaporizes Rock! You lose!")
elif human_gesture == "Paper":
    if ai_gesture == "Scissors":
        print("Scissors cuts Paper! You win!")
    elif ai_gesture == "Spock":
        print("Paper disproves Spock! You win!")
    elif ai_gesture == "Scissors":
        print("Scissors cuts Paper! You lose!")
    elif ai_gesture == "Lizard":
        print("Lizard eats Paper! You lose!")
elif human_gesture == "Scissors":
    if ai_gesture == "Paper":
        print("Scissors cuts Paper! You win!")
    elif ai_gesture == "Lizard":
        print("Scissors decapitates Lizard. You win!")
    elif ai_gesture == "Rock":
        print("Rock crushes Scissors! You lose!")
    elif ai_gesture == "Spock":
        print("Spock smashes Scissors! You lose!")
elif human_gesture == "Lizard":
    if ai_gesture == "Paper":
        print("Lizard eats Paper! You win!")
    elif ai_gesture == "Spock":
        print("Lizard poisons Spock. You win!")
    elif ai_gesture == "Rock":
        print("Rock crushes Lizard! You lose!")
    elif ai_gesture == "Scissors":
        print("Scissors decapitates Lizard! You lose!")
elif human_gesture == "Spock":
    if ai_gesture == "Scissors":
        print("Spock smashes Scissors! You win!")
    elif ai_gesture == "Rock":
        print("Spock vaporizes Rock. You win!")
    elif ai_gesture == "Lizard":
        print("Lizard poisons Spock! You lose!")
    elif ai_gesture == "Paper":
        print("Paper disproves Spock! You lose!")