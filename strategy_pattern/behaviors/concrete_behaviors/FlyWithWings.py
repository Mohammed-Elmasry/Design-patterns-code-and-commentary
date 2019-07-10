# this file defines the flyWithWings concrete class

from strategy_pattern.behaviors.FlyBehavior import Fly_Behavior


class FlyWithWings(Fly_Behavior):

    def fly(self):
        print("I'm flapping my wings")