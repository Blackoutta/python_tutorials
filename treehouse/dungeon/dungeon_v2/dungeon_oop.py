import random
import os
from jobs import *
from job_stats import *

CELLS = [(0,0), (1,0),(2,0),(3,0),(4,0),
         (0,1), (1,1),(2,1),(3,1),(4,1),
         (0,2), (1,2),(2,2),(3,2),(4,2),
         (0,3), (1,3),(2,3),(3,3),(4,3),
         (0,4), (1,4),(2,4),(3,4),(4,4)]



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Events:

    def check_str(self, monster):
        if dm.player.str > monster.str:
            return True
        else:
            return False

    def check_dex(self, monster):
        if dm.player.dex > monster.dex:
            return True
        else:
            return False

    def check_int(self, monster):
        if dm.player.int > monster.int:
            return True
        else:
            return False


    def event_1(self):
        clear_screen()
        input("一只无脑的僵尸出现在你面前。")
        input("僵尸: '人类...脑子...'")
        print("你会怎么做?")
        choice = input("1. 冲上去攻击它!\n2. 从它身旁绕过去\n3. 问: 1+1等于几?")
        if choice == '1':
            if Events.check_str(self, dm.zombie):
                input("你打败了僵尸！")
            else:
                damage = random.randint(10, 30)
                input("你不敌僵尸的力量，被他击倒在地后，慌忙逃窜.")
                input("你的HP减少了{}!".format(damage))
                dm.player.hp -= damage

        elif choice == '2':
            if Events.check_dex(self, dm.zombie):
                input("你迅速从僵尸身边饶了过去！")
            else:
                damage = random.randint(15, 40)
                input("僵尸比你想象中来得灵活，你被扑倒在地。")
                input("在被咬了一口之后，你挣脱了出来，落荒而逃。")
                input("你的HP减少了{}!".format(damage))
                dm.player.hp -= damage

        elif choice == '3':
            if Events.check_int(self, dm.zombie):
                input("僵尸: 啊啊，等于几...1+1等于几...啊啊啊啊啊!")
                input("僵尸的脑浆耗尽，倒在地上一动也不动了。")
            else:
                damage = random.randint(1, 25)
                input("当然是等于2!我讨厌别人把我当傻瓜!")
                input("你被僵尸的攻击擦过，慌忙逃了出去。")
                input("你的HP减少了{}!".format(damage))
                dm.player.hp -= damage




    def event_2(self):
        input("Hey, this is a placeholder for events 2!")

    EVENTS = [event_1, event_2]



class DungeonMaster():
    player_name = ''
    player = ''
    zombie = Zombie(zombie_stats)

    def get_player_name(self):
        while self.player_name == '':
            clear_screen()
            self.player_name = input("冒险者，请输入你的名字:  ")

    def get_player_job(self):
        clear_screen()
        while True:
            print("请选择你的职业:")
            print("Warrior, Mage, Thief")
            player_job = input(">>  ").lower()
            if player_job == "warrior":
                self.player = Warrior(self.player_name, warrior_stats)
                break
            elif player_job == "mage":
                self.player = Mage(self.player_name, mage_stats)
                break
            elif player_job == "thief":
                self.player = Thief(self.player_name, thief_stats)
                break
            else:
                input("请输入一个职业名称,并按'回车'确认!")
                clear_screen()
                continue


    def trigger_random_events(self):
        random.choice(Events.EVENTS)(self)

    def get_locations(self):
        return random.sample(CELLS, 3)

    def draw_map(self, player):
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

    def move_player(self, player, move):
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

    def get_moves(self, player):
        moves = ["LEFT", "RIGHT", "UP", "DOWN"]
        x, y = player
        if y == 0:
            moves.remove("UP")
        if y == 4:
            moves.remove("DOWN")
        if x == 0:
            moves.remove("LEFT")
        if x == 4:
            moves.remove("RIGHT")
        return moves

    def game_loop(self):
        monster, door, player = self.get_locations()
        playing = True
        while playing:
            clear_screen()
            self.draw_map(player)
            valid_moves = self.get_moves(player)
            print("冒险者: {}. 职业: {}".format(self.player_name, self.player.__class__.__name__))
            print("HP: {}".format(dm.player.hp))
            print("当前房间: {}".format(player))
            print("可移动方向: {}".format(','.join(valid_moves)))
            print("输入 'QUIT' 退出游戏")

            move = input(">  ")
            move = move.upper()

            if move == 'QUIT':
                print("\n ** 再见! ** \n")
                break
            if move in valid_moves:
                player = self.move_player(player, move)
                if player == door:
                    input("\n ** 恭喜！你逃出了地下城! ** \n")
                    playing = False
                self.trigger_random_events()
            else:
                input("\n **无效的指令!**\n")

        else:
            if input("再玩一次? [Y/n]  ").lower() != "n":
                self.game_loop()

# Program Runs
dm = DungeonMaster()
clear_screen()
print("欢迎来到地下城!")
input("按'回车'开始游戏!")
clear_screen()

dm.get_player_name()
dm.get_player_job()
dm.game_loop()
