from player import Player
import random
import time

class Ai(Player):
    def __init__(self, name):
        super().__init__(name)

    def chosen_gesture(self):
        self.selected_gesture = random.randint(0,4)
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        time.sleep(.25)
        self.selected_gesture = str(self.selected_gesture)
        time.sleep(.25)
        print(f"{self.name} has chosen {gesture_list[int(self.selected_gesture)]}")