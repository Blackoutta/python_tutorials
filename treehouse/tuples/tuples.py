course_minutes = {
"Python Basics": 232,
"Django Basics": 237,
"Flask Basics": 189,
"Java Basics": 133
}

# Iterating through a tuple
for course, minutes in course_minutes.items():
    print("{} is {} minutes long".format(course, minutes))

# The use of 'enumerate()', this will return multiple results, which is a big part of python
for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz", start = 1):
    print("{}: {}".format(index, letter))
