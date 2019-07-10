# this is the main module that'll run the strategy design pattern demo
import sys
print(sys.path)

from strategy_pattern.ducks import RubberDuck
from strategy_pattern.behaviors.concrete_behaviors import FlyRocketPower, Sweal
# declare behaviors
fly_rocket = FlyRocketPower()
skweal_behavior = Sweal()

# create a rubber duck and change its behaviors
rubberDuck = RubberDuck(fly_rocket, Sweal)
rubberDuck.fly()
rubberDuck.quack()