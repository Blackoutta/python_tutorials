# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.

# def wordcount(single_string):
#     single_list = single_string.lower().split()
#     print(single_list)
#     dict = {}
#     for selected_word in single_list:
#         count = 0
#         for word in single_list:
#             if word == selected_word:
#                 count += 1
#         # dict[selected_word] = count
#         dict.update({selected_word:count})
#     print(dict)
# wordcount("Hello Hello World sam sam sam sam tom tom")


def wordcount(string):
    key_list = string.lower().split()
    dict = {key: key_list.count(key) for key in key_list}
    print(dict)

wordcount("Hello Hello World")

# def wordcount(string):
#     dict = {}
#     key_list = string.lower().split()
#
#     for key in key_list:
#         if not key in dict:
#             dict[key] = 1
#         else:
#             dict[key] += 1
#
#     print(dict)
#
#
# wordcount("tom tom tom sam sam sam sam")

# def wordcount(string):
#     dict = {}
#     key_list = string.lower().split()
#
#     for key in key_list:
#         if not key in dict:
#             dict[key] = 1
#         else:
#             dict[key] += 1
#
#     print(dict)
#
#
# wordcount("tom tom tom sam sam sam sam")
