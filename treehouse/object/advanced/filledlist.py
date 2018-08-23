import copy


class FilledList(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__()
        # 这里的_可以让你无视range()没有的部分
        for _ in range(count):
            self.append(copy.copy(value))


fl = FilledList(9, 2)
fl2 = FilledList(2, [1,2,3])
