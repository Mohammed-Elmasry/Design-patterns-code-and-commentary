# this is a definition of the rocket flying
from strategy_pattern.behaviors import FlyBehavior

class FlyRocketPowered(FlyBehavior):


    def fly(self):
        print("I'm flying with rocket power!")