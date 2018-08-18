my_list = ["apple", 5.2, "dog", 8, True, False]

def combiner(mlist):
    words = ''
    nums = 0
    for i in mlist:
        if isinstance(i, str):
            words += i
        elif i == True:
            pass
        elif isinstance(i, (int, float)):
            nums += i
    output = words + str(nums)
    print(output)


combiner(my_list)