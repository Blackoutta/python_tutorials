import random

CELLS = [(0,0), (1,0),(2,0),(3,0),(4,0),
         (0,1), (1,1),(2,1),(3,1),(4,1),
         (0,2), (1,2),(2,2),(3,2),(4,2),
         (0,3), (1,3),(2,3),(3,3),(4,3),
         (0,4), (1,4),(2,4),(3,4),(4,4)]

def get_locations():
    return random.sample(CELLS, 3)

monster, door, player = get_locations()

print(" _" * 5) #Up Walls
tile = "|{}"
# for cell in CELLS:
#     x, y = cell
#     if x < 4:
#         line_end = ""
#         if cell == player:
#             output = tile.format("X")
#         else:
#             output = tile.format("_")
#     else: #Right Walls
#         line_end = "\n"
#         if cell == player:
#             output = tile.format("X|")
#         else:
#             output = tile.format("_|")
#     print(output, end = line_end)
for cell in CELLS:
    x, y = cell
    if x < 4:
        line_end = ""
        if player == cell:
            output = tile.format("X")
        else:
            output = tile.format("_")
    else:
        line_end = "\n"
        if player == cell:
            output = tile.format("X|")
        else:
            output = tile.format("_|")
    print(output, end = line_end)
