from player import Player
import random

class Ai(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def chosen_gesture(self):
        self.selected_gesture = str(random.randint(0,4))
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.selected_gesture = self.chosen_gesture
        print(f"{self.name} has chosen {gesture_list[int(self.chosen_gesture)]}")
