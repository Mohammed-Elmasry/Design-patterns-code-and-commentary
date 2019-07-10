# this is the main module that'll run the strategy design pattern demo

from .ducks.RubberDuck import *
from .behaviors.concrete_behaviors import FlyRocketPower, FlyWithWings, NoFly

# create a behavior
fly_rocket = FlyRocketPower()

# create a rubber duck and change its behaviors
rubberDuck = RubberDuck(fly_rocket)
rubberDuck.fly()
