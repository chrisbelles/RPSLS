from player import Player
import random

class Ai2(Player):
    def __init__(self, name, score):
        super().__init__()
        self.name = name
        self.score = 0
        self.selected_gesture = ""

    def chosen_gesture(self):
        self.selected_gesture = random.randint(0,4)
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.selected_gesture = str(self.selected_gesture)
        print(f"AI2 has chosen {gesture_list[int(self.selected_gesture)]}")
        # print(f"{self.name} has chosen {gesture_list[int(self.chosen_gesture)]}")
        # return str(self.chosen_gesture)
