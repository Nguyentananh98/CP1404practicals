""""
CP1404 -NGUYEN TAN ANH
JC950881
PRACTICAL 9
"""
import random
from Practical_9.car import Car


class UnreliableCar(Car):
    def __init__(self, name="", fuel=0, reliability=0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.randint(0, 100)
        if random_number < self.reliability:
            return super().drive(distance)


