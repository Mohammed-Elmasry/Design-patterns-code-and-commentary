# this file defines the flyWithWings concrete class

from strategy_pattern.behaviors import FlyBehavior


class FlyWithWings(FlyBehavior):

    def fly(self):
        print("I'm flapping my wings")