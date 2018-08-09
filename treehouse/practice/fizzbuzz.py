import math


while True:
    try:
        number = int(input("Please enter a number: "))
    except ValueError:
        print("Oh no, please input a number!")
        continue
    is_fizz = number%3 == 0
    is_buzz = number%5 == 0

# TODO: Make sure the number is an integer


# TODO: Print out the User's name and the number entered,
# making sure the two statements are on separate lines of output.
    print("The number is {}...".format(number))

# TODO: Compare the number the user gave with the different
# FizzBuzz conditions.
# *********************
# If the number is divisible by 3, print "is a Fizz number."
# If the number is divisible by 5, print "is a Buzz number."
# If the number is divisible by both 3 and 5, print "is a FizzBuzz number."
# Otherwise, print "is neither a fizzy or a buzzy number."
# *********************

    if is_fizz and is_buzz:
        print("It's a FizzBuzz!")
        continue
    elif is_buzz:
        print("It's a Buzz!")
        continue
    elif is_fizz:
        print("It's a Fizz!")
        continue
    else:
        print("It's neither a Fizz or a Buzz!")
        continue



# TODO: Define variables for is_fizz and is_buzz that stores
# a Boolean value of the condition. Remember that the modulo operator, %,
# can be used to check if there is a remainder.


# Using the variables, check the condition of the value, and print the necessary
# string
