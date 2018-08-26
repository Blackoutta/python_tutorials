import random
from functools import total_ordering

@total_ordering
class Die:
    def __init__(self, sides=2):
        if sides < 2:
            raise ValueError("Can't have fewer than two sides")
        self.sides = sides
        self.value = random.randint(1, sides)

    def __int__(self):
        return self.value

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return self + other

    def __repr__(self):
        return str(self.value)

    def __gt__(self, other):
        return int(self) > other


class D20(Die):
    def __init__(self, value=0):
        super().__init__(sides=20)
