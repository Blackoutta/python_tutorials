import random
from functools import total_ordering


@total_ordering   #只需要定义两个magic methods，便能识别接下来的所有比较符
class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("Must have at least 2 sides")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        self.value = value or random.randint(1, sides)

    def __int__(self):
        return self.value
    # equal to
    def __eq__(self, other):
        return int(self) == other
    # not equal to
    # def __ne__(self, other):
    #     return int(self) != other

    # greater than
    def __gt__(self, other):
        return int(self) > other
    # less than
    # def __lt__(self, other):
    #     return int(self) < other
    # # greater than or equal to
    # def __ge__(self, other):
    #     return int(self) > other or int(self) == other
    # # less than or equal to
    # def __le__(self, other):
    #     return int(self) < other or int(self) == other
    #
    # # 正向加法
    # def __add__(self, other):
    #     return int(self) + other
    #
    # # 反向加法
    # def __radd__(self, other):
    #     return int(self) + other

    # 在控制台查看class时，直接return value而不是object
    def __repr__(self):
        return str(self.value)

class D6(Die):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)


class D20(Die):
    def __init__(self, value=0):
        super().__init__(sides=20, value=value)



d6 = D6()
