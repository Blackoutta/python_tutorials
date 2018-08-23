# TODO: create a __str__ method in Letter class
# TODO: return "dot" for "."
# TODO: return "dash" for "_"
# TODO: join them with a hyphen


class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        output = []
        for i in self.pattern:
            if i == ".":
                output.append("dot")
            elif i == "_":
                output.append("dash")
        return '-'.join(output)

    def __iter__(self):
        yield from self.pattern

    @classmethod
    def from_string(cls, string=None):
        output = []
        string_ls = string.split("-")
        for i in string_ls:
            if i == "dash":
                output.append("_")
            elif i == "dot":
                output.append(".")
        return cls(output)



class S(Letter):
    def __init__(self):
        pattern = ['.', '.', '.', '_', "_"]
        super().__init__(pattern)




morse = Letter.from_string("dash-dot-dash-dot")
