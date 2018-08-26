from dice import D20

class Hand(list):

    def __init__(self, size=0, die_class=None, *args, **kwargs):
        super().__init__()
        if not die_class:
            raise ValueError("You must provide a die class")
        for _ in range(size):
            self.append(die_class())
        self.sort()


    @classmethod
    def roll(cls, roll_size):
        return cls(size=roll_size, die_class=D20)


    @property
    def total(self):
        return sum(self)
