# EXAMPLES:
# move((1, 1, 10), (-1, 0)) => (0, 1, 10)
# move((0, 1, 10), (-1, 0)) => (0, 1, 5)
# move((0, 9, 5), (0, 1)) => (0, 9, 0)

def move(player, direction):
    x, y, hp = player
    mx, my = direction
    if x + mx < 0 or x + mx > 9 or y + my < 0 or y + my > 9:
        hp -= 5
    else:
        x = x + mx
        y = y + my
    return x, y, hp
