from player import Player
import time


class Human(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.score = 0

def chosen_gesture(self):
    print("Choose 0 for Rock.")
    time.sleep(.5)
    print("Choose 1 for Paper.")
    time.sleep(.5)
    print("Choose 2 for Scissors.")
    time.sleep(.5)
    print("Choose 3 for Lizard.")
    time.sleep(.5)
    print("Choose 4 for Spock.")
    time.sleep(.5)
    self.chosen_gesture = input()
    gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    print(f"{self.name} has chosen {gesture_list[int(self.chosen_gesture)]}")