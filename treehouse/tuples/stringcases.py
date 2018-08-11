def stringcases(arg):
    string = str(arg)
    tuple = (string.upper(), string.lower(), string.title(), string[::-1])
    print(tuple)
stringcases("hello my name is yang")
