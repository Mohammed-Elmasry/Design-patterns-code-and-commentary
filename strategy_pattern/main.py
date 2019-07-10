# this is the main module that'll run the strategy design pattern demo
import sys
print(sys.path)

from strategy_pattern.ducks.RubberDuck import *
from strategy_pattern.behaviors.concrete_behaviors import FlyRocketPower, FlyWithWings, NoFly

# create a behavior
fly_rocket = FlyRocketPower()

# create a rubber duck and change its behaviors
rubberDuck = RubberDuck(fly_rocket)
rubberDuck.fly()
