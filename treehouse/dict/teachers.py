dict = {
"Kenneth Love": ["Python Basics", "Python Collections"],
"Andrew Chalkley": ["Jquery Basics", "Node.js Basics", "Jquery"]
}

def num_teachers(dict):
    return len(dict.keys())

def num_courses(dict):
    merge = []
    for i in dict.values():
        merge.extend(i)
    return len(merge)

def courses(dict):
    course_list = []
    for i in dict.values():
        course_list.extend(i)
    return course_list

def most_courses(dict):
    high = 0
    for teacher in dict:
        if len(dict[teacher]) > high:
            high = len(dict[teacher])
    # print(high)
    for teacher in dict:
        if len(dict[teacher]) == high:
            return teacher

# def stats(dict):
#     master_list = []
#     personal_dict = {}
#
#     for i in dict.keys():
#         personal_dict.update({i:0})
#     for i in dict:
#         personal_dict[i] = len(dict[i])
#     return (personal_dict)



# def stats(dict):
#     master_list = []
#     personal_dict = {}
#     placeholder = 0
#
#     for i in dict:
#         personal_dict.update({placeholder: [i, len(dict[i])]})
#         placeholder += 1
#     # print(personal_dict)
#     for i in personal_dict.values():
#         master_list.append(i)
#     print(master_list)
# stats(dict)

def stats(dict):
    ls = []
    for key, value in dict.items():
        ls.append([key, len(value)])
    print(ls)

stats(dict)
