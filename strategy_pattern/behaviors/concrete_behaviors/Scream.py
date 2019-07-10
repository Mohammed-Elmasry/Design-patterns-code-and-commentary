from strategy_pattern.behaviors.QuackBehavior import Quack_Behavior

class Scream(Quack_Behavior):

    def quack(self):
        print("ahhhhhhhhhh")