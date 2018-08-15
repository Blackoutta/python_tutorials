def add(*args): total = 0 for num in args: total += num print(total)
add(1,2,3,4,5)

def packer(**kwargs): print(kwargs)

packer(name = "kenneth", num = 42, spanish_inquisition = None)

def unpacker(first_name, last_name): print("Hi, you are {} {},
right?".format(first_name, last_name))

unpacker(**{"last_name": "Love", "first_name": "Kenneth"})

#
#dsafassssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
