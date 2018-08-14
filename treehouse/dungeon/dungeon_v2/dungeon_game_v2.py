import random
import os
import events
import system_feature
import characters

CELLS = [(0,0), (1,0),(2,0),(3,0),(4,0),
         (0,1), (1,1),(2,1),(3,1),(4,1),
         (0,2), (1,2),(2,2),(3,2),(4,2),
         (0,3), (1,3),(2,3),(3,3),(4,3),
         (0,4), (1,4),(2,4),(3,4),(4,4)]



# def draw_map():


# Define functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_locations():
    return random.sample(CELLS, 3)


def move_player(player, move):
    # get player get_locations
    # if move == left, x-1
    # if move == right, x+1
    # if move == up, y-1
    # if move == down, y+1
    x, y = player
    if move == "LEFT":
        x -= 1
    elif move == "RIGHT":
        x += 1
    elif move == "UP":
        y -= 1
    elif move == "DOWN":
        y += 1
    return x, y
    return player


def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player
    # if player's y == 0, can't move UP
    # if player's y == 4, can't move DOWN
    # if player's x == 0, can't move LEFT
    # if player's x == 4, they can't move RIGHT
    if y == 0:
        moves.remove("UP")
    if y == 4:
        moves.remove("DOWN")
    if x == 0:
        moves.remove("LEFT")
    if x == 4:
        moves.remove("RIGHT")
    return moves


def draw_map(player):
    print(" _" * 5) #Up Walls
    tile = "|{}"
    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else: #Right Walls
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end = line_end)

def event_check():
    if random.randint(1, 100) > 70:
        events.event_1(**characters.GHOST)
    elif random.randint(1, 100) > 50:
        events.battle(**characters.GHOST)


def game_loop():
    monster, door, player = get_locations()
    playing = True
    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_moves(player)
        print("You're currently in room {}".format(player))
        print("You can move {}".format(','.join(valid_moves)))
        print("Enter QUIT to quit")

        move = input(">  ")
        move = move.upper()

        if move == 'QUIT':
            print("\n ** See you next time! ** \n")
            break
        if move in valid_moves:
            player = move_player(player, move)
            if player == door:
                input("\n ** Congratulations! You have escaped the dungeon! ** \n")
                playing = False
            else:
                event_check()
        else:
            input("\n **Invalid Move!**\n")

    else:
        if input("Play again? [Y/n]  ").lower() != "n":
            game_loop()









# Program Runs

clear_screen()
print("Welcome to the dungeon!")
input("Press return to start!")
clear_screen()
game_loop()
