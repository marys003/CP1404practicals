from prac_09.car import Car

import random

class UnreliableCar(Car):
    """Specialized version of Car with reliability attribute."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

        def drive(self, distance):
            """Drive like parent Car but with reliability as well."""
            if random.randint(0, 100) < self.reliability:
                distance_driven = super().drive(distance)
            else:
                distance_driven = 0
            return distance_driven