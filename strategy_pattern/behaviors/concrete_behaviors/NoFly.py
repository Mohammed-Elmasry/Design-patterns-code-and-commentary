# this file defines the noFly Behavior

from strategy_pattern.behaviors import FlyBehavior

class FlyNoWay(FlyBehavior):

    def fly(self):
        print("I can't fly")