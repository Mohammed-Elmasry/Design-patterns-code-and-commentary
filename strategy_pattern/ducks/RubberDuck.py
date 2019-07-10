# this defines a rubber duck class
from strategy_pattern.ducks.Duck import DuckBase


class RubberDucky(DuckBase):


    quack_behavior = None
    fly_behavior = None

    def __init__(self, fly_bahvior, quack_behavior):
        self.quack_behavior = quack_behavior
        self.fly_behavior = fly_bahvior

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
        self.quack_behavior.quack()