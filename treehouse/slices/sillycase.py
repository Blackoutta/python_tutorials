def sillycase(string):
    string_len = len(string)//2
    first_half_lower = string[0:string_len].lower()
    second_half_upper = string[string_len:].upper()
    final_number = first_half_lower + second_half_upper
    print(final_number)

sillycase("treehouse")
sillycase("huyangyi")
