# this file defines the noFly Behavior

from ..FlyBehavior import FlyBehavior

class FlyNoWay(FlyBehavior):

    def fly(self):
        print("I can't fly")