# this file defines the flyWithWings concrete class

from ..FlyBehavior import FlyBehavior


class FlyWithWings(FlyBehavior):

    def fly(self):
        print("I'm flapping my wings")