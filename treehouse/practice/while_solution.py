# Problem 1: Warm the oven
# Write a while loop that checks to see if the oven
# is 350 degrees. If it is, print "The oven is ready!"
# If it's not, increase current_oven_temp by 25 and print
# out the current temperature.

current_oven_temp = 75

while current_oven_temp < 350:
    current_oven_temp += 25
    print(current_oven_temp)
else:
    print("The oven is ready!")

# Solution 1 here

# Problem 2: Total and average
# Complete the following function so that it asks for
# numbers from the user until they enter 'q' to quit.
# When they quit, print out the list of numbers,
# the sum and the average of all of the numbers.

def total_and_average():
    print("\nEnter 'q' to calculate the results.")
    numbers = []
    sum = 0
    while True:
        user_input = input("please enter a number:  ")

        if user_input != 'q':
            try:
                numbers.append(int(user_input))
            except ValueError:
                print("You must enter an integer.")
        else:
            print("List of your numbers: {}".format(numbers))
            for i in numbers:
                sum += i
            try:
                average = sum / len(numbers)
            except ZeroDivisionError:
                break
            print("Sum: {}".format(sum))
            print("Average: {}".format(average))
            break





    # Solution 2 here

total_and_average()

# Problem 3: Missbuzz
# Write a while loop that increments current by 1
# If the new number is divisible by 3, 5, or both,
# print out the number. Otherwise, skip it.
# Break out of the loop when current is equal to 101.

current = 1
print("\nMissbuzz:")
while True:
    current += 1
    if current % 3 == 0:
        print(current)
    elif current % 5 == 0:
        print(current)
    elif current % 3 == 0 and current % 5 == 0:
        print(current)
    elif current == 101:
        break
    else:
        pass



# Solution 3 here
