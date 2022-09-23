from player import Player
import random

class Ai2(Player):
    def __init__(self, name, score):
        super().__init__()
        self.name = name
        self.score = 0

    def chosen_gesture(self):
        self.chosen_gesture = (random.randint(0,4))
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        # self.chosen_gesture = self.selected_gesture
        print(f"AI has chosen {gesture_list[int(self.chosen_gesture)]}")
        # print(f"{self.name} has chosen {gesture_list[int(self.chosen_gesture)]}")
        return self.chosen_gesture
