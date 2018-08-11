# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

def combo(a, b):
    output = []
    for i in range(len(a)):
        tup = (a[i], b[i])
        output.append(tup)
    print(output)



combo([1,2,3], "abc")
