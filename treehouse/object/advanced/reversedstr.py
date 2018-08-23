class ReversedStr(str):
    # __new__是一个 class method，它会对class起作用，而不是instance
    # __new__用在 immutable 上
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self

me = ReversedStr('hello')
