class Player:
    def __init__(self, name, stats):
        self.name = name

        for key, value in stats.items():
            setattr(self, key, value)

class Zombie:
    def __init__(self, stats):

        for key, value in stats.items():
            setattr(self, key, value)

class Fatty:
    def __init__(self, stats):

        for key, value in stats.items():
            setattr(self, key, value)

class Necromancer:
    def __init__(self, stats):

        for key, value in stats.items():
            setattr(self, key, value)
