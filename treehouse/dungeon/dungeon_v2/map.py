import random
CELLS = [(0,0), (1,0),(2,0),(3,0),(4,0),
         (0,1), (1,1),(2,1),(3,1),(4,1),
         (0,2), (1,2),(2,2),(3,2),(4,2),
         (0,3), (1,3),(2,3),(3,3),(4,3),
         (0,4), (1,4),(2,4),(3,4),(4,4)]



class Map:

    def __init__(self):
        self.player_location, self.key_1, self.key_2, self.key_3, self.door = random.sample(CELLS, 5)

    def draw_map(self):
        print(" _" * 5) #Up Walls
        tile = "|{}"
        for cell in CELLS:
            x, y = cell
            if x < 4:
                line_end = ""
                if cell == self.player_location:
                    output = tile.format("X")
                elif cell == self.door:
                    output = tile.format("O")
                # elif cell == self.key_1:
                #     output = tile.format("J")
                # elif cell == self.key_2:
                #     output = tile.format("J")
                # elif cell == self.key_3:
                #     output = tile.format("J")
                else:
                    output = tile.format("_")
            else: #Right Walls
                line_end = "\n"
                if cell == self.player_location:
                    output = tile.format("X|")
                elif cell == self.door:
                    output = tile.format("O|")
                # elif cell == self.key_1:
                #     output = tile.format("J|")
                # elif cell == self.key_2:
                #     output = tile.format("J|")
                # elif cell == self.key_3:
                #     output = tile.format("J|")
                else:
                    output = tile.format("_|")
            print(output, end = line_end)
        print("\n X 代表 玩家\n O代表 地牢大门")

    def get_moves(self):
        moves = ["LEFT", "RIGHT", "UP", "DOWN"]
        x, y = self.player_location
        if y == 0:
            moves.remove("UP")
        if y == 4:
            moves.remove("DOWN")
        if x == 0:
            moves.remove("LEFT")
        if x == 4:
            moves.remove("RIGHT")
        return moves


    def move_player(self, move):
        x, y = self.player_location
        if move == "LEFT":
            x -= 1
        elif move == "RIGHT":
            x += 1
        elif move == "UP":
            y -= 1
        elif move == "DOWN":
            y += 1
        return x, y
        return self.player_location






if __name__ == "__main__":
    current_map = Map()
    current_map.draw_map()
