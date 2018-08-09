def odds(iterable):
    return iterable[1::2]

def first_4(iterable):
    return iterable[0:4]

def first_and_last_4(iterable):
    return iterable[:4] + iterable[-4:]

def reverse_evens(iterable):
    evens = iterable[::2]
    reverse = evens[::-1]
    return reverse
