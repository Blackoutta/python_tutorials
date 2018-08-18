from job_stats import *


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


class DungeonMaster:

    def check_str(self, player1, player2):
        if player1.str > player2.str:
            print("{} wins! what a formidable {}!".format(player1.name, player1.__class__.__name__))
        elif player1.dex == player2.dex:
            print("It's a draw!")
        else:
            print("{} wins! what a formidable {}!".format(player2.name, player2.__class__.__name__))

    def check_dex(self, player1, player2):
        if player1.dex > player2.dex:
            print("{} wins! what a cunning {}!".format(player1.name, player1.__class__.__name__))
        elif player1.dex == player2.dex:
            print("It's a draw!")
        else:
            print("{} wins! what a cunning {}!".format(player2.name, player2.__class__.__name__))


    def check_int(self, player1, player2):
        if player1.int > player2.int:
            print("{} wins! what a clever {}!".format(player1.name, player1.__class__.__name__))
        elif player1.int == player2.int:
            print("It's a draw!")
        else:
            print("{} wins! what a clever {}!".format(player2.name, player2.__class__.__name__))

yang = Warrior("Yang", warrior_stats)
jack = Mage("Jack", mage_stats)
emi = Thief("Emi", thief_stats)

dm = DungeonMaster()