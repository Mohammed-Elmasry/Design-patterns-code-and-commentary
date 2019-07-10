# define the sound of a rubber duck
from strategy_pattern.behaviors.QuackBehavior import QuackBehavior


class Skweal(QuackBehavior):


    def Quack(self):
        print("skweal skweal")