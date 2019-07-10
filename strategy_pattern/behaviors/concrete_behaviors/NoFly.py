# this file defines the noFly Behavior

from strategy_pattern.behaviors.FlyBehavior import Fly_Behavior

class FlyNoWay(Fly_Behavior):

    def fly(self):
        print("I can't fly")