class RaceCar:

    def __init__(self, color, fuel_remaining, **kwargs):
        self.laps = 0
        self.color = color
        self.fuel_remaining = fuel_remaining
        for key, value in kwargs.items():
            setattr(self, key, value)

    def run_lap(self, length):
        self.fuel_remaining -= length * 0.125
        self.laps += 1
