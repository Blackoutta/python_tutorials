# kwargs = key word arguments
def packer(**kwargs):
    print(kwargs)
packer(name = "kenneth", num = 42, spanish_inquisition = None)


def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi,{}{}!".format(first_name, last_name))
    else:
        print("Hi, no name!")
unpacker(**{"last_name": "Love", "first_name": "Kenneth"})
