sodas = ["Pepsi", "Cherry Coke Zero", "Sprite"]
chips = ["Doritos", "Fritos"]
candy = ["Snickers", "MMs", "Twizzlers"]

while True:
    choice = input("Would you like a SODA, some CHIPSS, or a CANDY?  ").lower()
    try:
        if choice == "soda":
            snack = sodas.pop()
        elif choice == "chips":
            snack = chips.pop()
        elif choice == "candy":
            snack = candy.pop()
        else:
            print("Sorry, I didn't understand that.")
            continue
    except IndexError:
        print("{} are all sold out!".format(choice))
        continue
    print("Here is your {}: {}!".format(choice, snack))
