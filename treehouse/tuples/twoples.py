
# Packing args into tuple
def multiply(base, *args):
    product = base
    for num in args:
        product *= num
    print(product)

multiply(1, 2, 3, 4, 5, 2)


def add(*args):
    total = 0
    for num in args:
        total += num
    print(total)
add(1,2,3,4,5)
