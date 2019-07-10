# this is a definition of the rocket flying
from ..FlyBehavior import FlyBehavior

class FlyRocketPowered(FlyBehavior):


    def fly(self):
        print("I'm flying with rocket power!")