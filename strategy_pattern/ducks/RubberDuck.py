# this defines a rubber duck class
from . import Duck


class RubberDuck(Duck):

    def __init__(self, fly_bahvior, quack_behavior):
        self.quack_behavior = quack_behavior
        self.fly_behavior = fly_bahvior

    quack_behavior = None
    fly_behavior = None

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
        self.quack_behavior.quack()