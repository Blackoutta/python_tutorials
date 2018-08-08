# infinite loop and how to break it or continue it
# Create a new empty list named shopping_list
shopping_list = []

#Create a function named add_to_list that declares a parameter named item
    #Add the item to the list

def add_to_list(item):
    shopping_list.append(item)
    # notify user that the item was add and state the number of items in the list currently
    print("Your item has been added, you currently have {} items in your list!".format(len(shopping_list)))

# Define a function named show_list that prints all the items in the list
def show_list():
    for item in shopping_list:
        print("* " + item)

def show_help():
    print("What should we pick up at the store?")
    print("""
Enter "DONE" to stop adding items.
Enter 'HELP' for this help.
Enter 'LIST' to show the in-cart items.
""")

show_help()
while True:
    new_item = input("> ")
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'LIST':
        print("===> You have the following items in your cart: <===")
        show_list()
        continue
show_list() # when uswer is done
    # Call add_to_list with new_item
add_to_list(new_item)
