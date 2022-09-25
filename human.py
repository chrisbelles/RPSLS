from player import Player
import time


class Human(Player):
    def __init__(self, name, score):
        super().__init__()
        self.name = name
        self.score = 0
        self.selected_gesture = ""

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
        self.chosen_gesture = input("Please enter make your selection! ")
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.selected_gesture = self.chosen_gesture
        print(f"Player 1 has chosen {gesture_list[int(self.chosen_gesture)]}")
        # return str(self.chosen_gesture)