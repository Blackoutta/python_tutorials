# Columns: Name, Day/Month, Celebrates, Age
BIRTHDAYS = (
    ("James", "9/8", True, 9),
    ("Shawna", "12/6", True, 22),
    ("Amaya", "28/2", False, 8),
    ("Kamal", "29/4", True, 19),
    ("Sam", "16/7", False, 22),
    ("Xan", "14/3", False, 34),
)

# Problem 1: Celebrations
# Loop through all of the people in BIRTHDAYS
# If they celebrate their birthday, print out
# "Happy Birthday" and their name
print("Task 1 - Celebration:")
for person in BIRTHDAYS:
    if True in person:
        print("Happy Birthday! " + person[0] + "!")

# Problem 2: Half birthdays
# Loop through all of the people in BIRTHDAYS
# Calculate their half birthday (six months later)
# Print out their name and half birthday
print("Task 2 - Half Birthday:")
for person in BIRTHDAYS:
    birth_date = person[1].split("/")
    birth_day = int(birth_date.pop())
    output = []
    if birth_day > 6:
        birth_day -= 6
        birth_date.append(str(birth_day))
    else:
        birth_day += 6
        birth_date.append(str(birth_day))
    birth_date = '/'.join(birth_date)
    output.append(person[0])
    output.append(birth_date)
    print(output)



# Problem 3: Only school year birthdays
# Loop through the people in BIRTHDAYS
# If their birthday is between September (9)
# And June (6), print their name
print("School Year Birthday: ")
for person in BIRTHDAYS:
    name = person[0]
    school_year = [9,10,11,12,1,2,3,4,5,6]
    birth_date = person[1].split("/")
    birth_date[1] = int(birth_date[1])
    if birth_date[1] in school_year:
        print(name)




# Problem 4: Wishing stars
# Loop through BIRTHDAYS
# If the person celebrates their birthday,
# AND their age is 10 or less,
# Print out their name and as many stars as their age
print("Wishing Stars:")
for person in BIRTHDAYS:
    name = person[0]
    age = person[3]
    if age <= 10:
        print(name + ' *' * age)
