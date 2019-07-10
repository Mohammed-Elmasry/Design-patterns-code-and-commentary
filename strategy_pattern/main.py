# this is the main module that'll run the strategy design pattern demo

from strategy_pattern.ducks.RubberDuck import RubberDucky
from strategy_pattern.behaviors.concrete_behaviors import FlyRocketPower, Skweal

# declare behaviors
fly_rocket = FlyRocketPower()
skweal_behavior = Skweal()

# create a rubber duck and change its behaviors
myRubberDuck = RubberDucky(fly_rocket, skweal_behavior)
myRubberDuck.fly()
myRubberDuck.quack()