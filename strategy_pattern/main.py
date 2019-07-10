# this is the main module that'll run the strategy design pattern demo

from strategy_pattern.ducks.RubberDuck import RubberDucky
from strategy_pattern.behaviors.concrete_behaviors.FlyRocketPower import FlyRocketPowered
from strategy_pattern.behaviors.concrete_behaviors.NoFly import FlyNoWay
from strategy_pattern.behaviors.concrete_behaviors.Skweal import Skweal

# declare behaviors
fly_rocket = FlyRocketPowered()
skweal_behavior = Skweal()

# create a rubber duck and change its behaviors
myRubberDuck = RubberDucky(fly_rocket, skweal_behavior)
myRubberDuck.fly()
myRubberDuck.quack()

no_fly = FlyNoWay()

# create another kind of flying behavior and assign it to the rubber duck

myRubberDuck.set_fly_behavior(no_fly)
myRubberDuck.fly()
myRubberDuck.quack()

# create another kind of quack behavior and assign it to the rubber duck

