def disemvowel(word):
    word_into_list = list(word)
    try:
        while "a" in word_into_list:
            word_into_list.remove("a")
        while "e" in word_into_list:
            word_into_list.remove("e")
        while "i" in word_into_list:
            word_into_list.remove("i")
        while "o" in word_into_list:
            word_into_list.remove("o")
        while "u" in word_into_list:
            word_into_list.remove("u")
        while "A" in word_into_list:
            word_into_list.remove("A")
        while "E" in word_into_list:
            word_into_list.remove("E")
        while "I" in word_into_list:
            word_into_list.remove("I")
        while "O" in word_into_list:
            word_into_list.remove("O")
        while "U" in word_into_list:
            word_into_list.remove("U")
    except ValueError:
        pass
    list_into_word = ''.join(word_into_list)
    print(list_into_word)

user_word = input("Please enter a word to be disemvoweled:  ")
disemvowel(user_word)
