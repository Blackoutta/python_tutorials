import random
import os

# TODO: draw grid
# TODO: pick random location for player
# TODO: random location for exit door
# TODO: random location for the mosnter
# TODO: draw player in the grid
# TODO: take input for movement
# TODO: move player unless invalid move (past edges of grid)
# TODO: check for win/loss
# TODO: clear screen and redraw grid

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



def game_loop():
    monster, door, player = get_locations()
    playing = True
    while playing:
        clear_screen()
        draw_map(player)
        valid_moves = get_moves(player)
        print("\n当前房间： {}".format(player))
        print("可移动方向：{}".format(','.join(valid_moves)))
        print("输入 'QUIT' 来退出")

        move = input(">  ")
        move = move.upper()

        if move == 'QUIT':
            print("\n ** 下次再见 ** \n")
            break
        if move in valid_moves:
            player = move_player(player, move)
            if player == monster:
                input("\n ** 你被怪物吃掉了！ ** \n")
                playing = False
            if player == door:
                input("\n ** 恭喜！你逃出了地下城！ ** \n")
                playing = False
        else:
            input("\n **你不能这么移动**\n")

    else:
        if input("再玩一次？ [Y/n]  ").lower() != "n":
            game_loop()









# Program Runs

clear_screen()
print("欢迎来到轻松地下城！")
input("按任意键开始游戏！")
clear_screen()
game_loop()




    # Good move
    # Bad move
    # door? win
    # monster? lose
    # otherwise loop back
