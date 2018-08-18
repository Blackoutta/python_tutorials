import job_stats

class Job:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class Warrior(Job):

    def __init__(self, name, stats, **kwargs):
        self.name = name
        for key, value in stats.items():
            setattr(self, key, value)
        super().__init__(**kwargs)


class Mage(Job):

    def __init__(self, name, stats, **kwargs):
        self.name = name
        for key, value in stats.items():
            setattr(self, key, value)
        super().__init__(**kwargs)


class Thief(Job):

    def __init__(self, name, stats, **kwargs):
        self.name = name
        for key, value in stats.items():
            setattr(self, key, value)
        super().__init__(**kwargs)

class Zombie(Job):

    def __init__(self, stats, **kwargs):
        self.name = "僵尸"
        for key, value in stats.items():
            setattr(self, key, value)
        super().__init__(**kwargs)
