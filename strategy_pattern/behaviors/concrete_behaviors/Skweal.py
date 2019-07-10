# define the sound of a rubber duck
from strategy_pattern.behaviors.QuackBehavior import Quack_Behavior


class Skweal(Quack_Behavior):


    def quack(self):
        print("skweal skweal")