# TODO Create an empty list to maintain the player names
players = []

# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'
while True:
    query_add_players = input("Would you like to add a new player? YES/NO:  ")
    if query_add_players.lower() == "yes":
        add_player = input("Please enter the new player's name:  ")
        players.append(add_player)
    elif query_add_players.lower() == "no":
        print("There are {} players in the team right now.".format(len(players)))
        player_number = 1
        for player in players:
            print("Player{}: ".format(player_number) + player)
            player_number += 1
        break
    else:
        print("Sorry, I didn't understand that.")
        continue

# TODO print the number of players on the team


# TODO Print the player number and the player name
# The player number should start at the number one



# TODO Select a goalkeeper from the above roster
while True:
    query_goalkeeper = input("Of the selected players, who will be the goalkeeper? 1-{}:  ".format(len(players)))
    try:
        print("It's decided, the goal keeper is {}!".format(players[int(query_goalkeeper) - 1]))
    except ValueError:
        print("Please enter a valid number!")
        continue
    except IndexError:
        print("Please enter a valid number!")
        continue
    break




# TODO Print the goal keeper's name
# Remember that lists use a zero based index
