
# | or .union(*others) - all of the items from all of the sets
# & or .intersection(*others) - all of the common items between all of the sets
# - or .difference(*others) - all of the items in the first set that are not in the other sets
# ^ or .symmetric_difference(other) - all of the items that are not shared by the two sets
# (also: notice how those are using *others? That's a tuple of other sets. See, I told you that pattern was everywhere!)
COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(supplied_set):
    course_set = set({})
    output = set({})
    for key, value in COURSES.items():
        if supplied_set & value:
            output.add(key)
    print(list(output))
    # return list(output)

covers({"conditions", "input"})


def covers_all(supplied_set):
    course_set = set({})
    output = set({})
    for key, value in COURSES.items():
        if supplied_set & value:
            output.add(key)
        if supplied_set - value:
            output.remove(key)
    print(output)
    # return list(output)

covers_all({"conditions", "input"})
