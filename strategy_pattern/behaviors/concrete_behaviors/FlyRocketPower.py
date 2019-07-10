# this is a definition of the rocket flying
from strategy_pattern.behaviors.FlyBehavior import Fly_Behavior

class FlyRocketPowered(Fly_Behavior):


    def fly(self):
        print("I'm flying with rocket power!")