from distutils.log import error
from msilib.schema import Error
import time
from human import Human
from ai import Ai
# from ai2 import Ai2
# from human2 import Human2


class Game():
    def __init__(self):
        self.player_one = ""
        self.player_two = ""

    def display_welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock")
        print("")
        time.sleep(.5)
        print("Best of 3 will be the winner")
        print("Use the number keys to choose your attack")
        print("")
        print("")
        time.sleep(.25)
        print("Rock crushes Scissors")
        time.sleep(.25)
        print("Scissors cuts Paper")
        time.sleep(.25)
        print("Paper covers Rock")
        time.sleep(.25)
        print("Rock crushes Lizard")
        time.sleep(.25)
        print("Lizard poisons Spock")
        time.sleep(.25)
        print("Spock smashes Scissors")
        time.sleep(.25)
        print("Scissors decapitates Lizard")
        time.sleep(.25)
        print("Lizard eats Paper")
        time.sleep(.25)
        print("Paper disproves Spock")
        time.sleep(.25)
        print("Spock vaporizes Rock")
        print("")
        print("")
        

    def play_game(self):
        input_validation = True
        while input_validation:          
          players = input("How many players? 1 (Human vs. AI), 2 (Human vs. Human), or 3 (Ai vs. Ai)? ")    
          if players == "1":
              self.player_one = Human("Player One", 0)            
              self.player_two = Ai("Player Two",0)
              input_validation = False           
          elif players == "2":
              self.player_one = Human("Player One",0)            
              self.player_two = Human("Player Two",0)
              input_validation = False            
          elif players == "3":
              self.player_one = Ai("Player One", 0)            
              self.player_two = Ai("Player Two", 0)
              input_validation = False 
          else:
              print("Invalid Entry. Please try again.")

            


        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.chosen_gesture()
            self.player_two.chosen_gesture()


            if self.player_one.selected_gesture == self.player_two.selected_gesture:
                print(f"Both players selected {self.player_one.selected_gesture}. It's a tie!")
            elif self.player_one.selected_gesture == "0":
                if self.player_two.selected_gesture == "2":
                     self.player_one.score += 1
                     print("Rock crushes Scissors! You win!")
                elif self.player_two.selected_gesture == "3":
                     self.player_one.score += 1
                     print("Rock crushes Lizard! You win!")
                elif self.player_two.selected_gesture == "1":
                     self.player_two.score += 1
                     print("Paper covers Rock! You lose!")
                elif self.player_two.selected_gesture == "4":
                     self.player_two.score += 1
                     print("Spock vaporizes Rock! You lose!")
            elif self.player_one.selected_gesture == "1":
                if self.player_two.selected_gesture == "2":
                     self.player_one.score += 1
                     print("Scissors cuts Paper! You win!")
                elif self.player_two.selected_gesture == "4":
                     self.player_one.score += 1
                     print("Paper disproves Spock! You win!")
                elif self.player_two.selected_gesture == "0":
                     self.player_two.score += 1
                     print("Paper! You lose!")
                elif self.player_two.selected_gesture == "3":
                     self.player_two.score += 1
                     print("Lizard eats Paper! You lose!")
            elif self.player_one.selected_gesture == "2":
                if self.player_two.selected_gesture == "1":
                     self.player_one.score += 1
                     print("Scissors cuts Paper! You win!")
                elif self.player_two.selected_gesture == "3":
                     self.player_one.score += 1
                     print("Scissors decapitates Lizard. You win!")
                elif self.player_two.selected_gesture == "0":
                     self.player_two.score += 1
                     print("Rock crushes Scissors! You lose!")
                elif self.player_two.selected_gesture == "4":
                     self.player_two.score += 1
                     print("Spock smashes Scissors! You lose!")
            elif self.player_one.selected_gesture == "3":
                if self.player_two.selected_gesture == "1":
                     self.player_one.score += 1
                     print("Lizard eats Paper! You win!")
                elif self.player_two.selected_gesture == "4":
                     self.player_one.score += 1
                     print("Lizard poisons Spock. You win!")
                elif self.player_two.selected_gesture == "0":
                     self.player_two.score += 1
                     print("Rock crushes Lizard! You lose!")
                elif self.player_two.selected_gesture == "2":
                    self.player_two.score += 1
                    print("Scissors decapitates Lizard! You lose!")
            elif self.player_one.selected_gesture == "4":
                if self.player_two.selected_gesture == "2":
                     self.player_one.score += 1
                     print("Spock smashes Scissors! You win!")
                elif self.player_two.selected_gesture == "0":
                     self.player_one.score += 1
                     print("Spock vaporizes Rock. You win!")
                elif self.player_two.selected_gesture == "3":
                     self.player_two.score += 1
                     print("Lizard poisons Spock! You lose!")
                elif self.player_two.selected_gesture == "1":
                     self.player_two.score += 1
                     print("Paper disproves Spock! You lose!")


    def declare_winner(self):
          if self.player_one.score == 2:
               print("Player One is the winner!")
          elif self.player_two.score == 2:
               print("Player Two is the winner!")

    def rematch(self):
     input_validation = True
     while input_validation:  
          play_again = input("Would you like to play again? y/n ")
          if play_again == "y":
               self.display_welcome()
               self.play_game()
               self.declare_winner()
               self.rematch()
               input_validation = False
          elif play_again == "n":
               print("Thanks for playing!")
               input_validation = False
          else:
               print("Invalid Entry. Please try again.")
