from player import Player
import time


class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def chosen_gesture(self):
        print("Choose 0 for Rock.")
        time.sleep(.25)
        print("Choose 1 for Paper.")
        time.sleep(.25)
        print("Choose 2 for Scissors.")
        time.sleep(.25)
        print("Choose 3 for Lizard.")
        time.sleep(.25)
        print("Choose 4 for Spock.")
        time.sleep(.25)
        self.selected_gesture = input("Please enter make your selection! ")
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

        input_validation = True
        while input_validation:
            if self.selected_gesture == "0" or self.selected_gesture == "1" or self.selected_gesture == "2" or self.selected_gesture == "3" or self.selected_gesture == "4":
                print(f"{self.name} has chosen {gesture_list[int(self.selected_gesture)]}")
                input_validation = False
            else:
                self.selected_gesture = input("Please try again. Select 0, 1, 2, 3, or 4. ")