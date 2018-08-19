import os
import sys
from characters import *
from job_stats import *
from map import *
from events import *
from system import clear_screen

current_events = Events()

def game_loop():
    # 游戏开场介绍 & 玩家姓名，职业设置
    clear_screen()
    input("欢迎来到地下城！")
    while True:
        clear_screen()
        player_name = input("请输入你的名字:  ")
        if player_name == '':
            input("**请输入一个有效的名称**")
            continue
        elif len(player_name) > 10:
            input("**名称过长，请重新输入**")
            continue
        else:
            break


    while True:
        clear_screen()
        print("1. 圣堂骑士\n2. 神秘学者\n3. 盗贼头领")
        player_job = input("\n请选择你的职业(输入数字并按回车确认):  ")

        if player_job == "1":
            current_player = Player(player_name, warrior_stats)
            break
        elif player_job == "2":
            current_player = Player(player_name, mage_stats)
            break
        elif player_job == "3":
            current_player = Player(player_name, thief_stats)
            break
        else:
            input("**请输入数字并按回车来选择你的职业。**")
            continue
    input("你好，{}，你的职业是{}，让我们开始冒险吧！".format(player_name, current_player.job_name))
    playing = True
    current_map = Map()

    #游戏正式开始
    while playing:
        clear_screen()
        current_map.draw_map()
        valid_moves = current_map.get_moves()
        print("\n冒险者: {}. 职业: {}\n".format(current_player.name, current_player.job_name))
        print("*" * 25)
        print("  HP: {}/{}  恢复剂: {}  钥匙: {}".format(current_player.hp, current_player.max_hp, current_player.potion, current_player.key))
        print("*" * 25)
        print("\n当前房间: {}".format(current_map.player_location))
        print("可移动方向: {}".format(','.join(valid_moves)))
        print("\n输入 'QUIT' 退出游戏")
        print("输入 'HEAL'会消耗恢复剂并回复HP")

        move = input(">>>  ")
        move = move.upper()

        if move == 'QUIT':
            print("\n ** 再见! ** \n")
            break
        elif move == 'HEAL':
            heal = random.randint(20, 35)
            if current_player.potion <= 0:
                input("**恢复剂不足！**")
            elif current_player.hp == current_player.max_hp:
                input("**你不需要治疗！**")
            elif current_player.hp < current_player.max_hp:
                post_heal_hp = current_player.hp + heal
                current_player.potion -= 1
                if post_heal_hp > current_player.max_hp:
                    current_player.hp = current_player.max_hp
                    input("你恢复了{}点HP!".format(heal - (post_heal_hp - current_player.max_hp)))
                else:
                    current_player.hp = post_heal_hp
                    input("你恢复了{}点HP!".format(heal))
        elif move in valid_moves:
            current_map.player_location = current_map.move_player(move)
            if current_map.player_location == current_map.door:
                clear_screen()
                input("\n你找到了地下城的出口，厚重的石门上有三个钥匙孔。")
                input("你使劲推门，但它纹丝不动，看来你需要凑齐三把钥匙才行。")
                # playing = False
            elif current_map.player_location == current_map.key_1:
                clear_screen()
                input("\n你找到了一把钥匙！")
                current_map.key_1 = ''
                current_player.key += 1
            elif current_map.player_location == current_map.key_2:
                clear_screen()
                input("\n你找到了一把钥匙！")
                current_map.key_2 = ''
                current_player.key += 1

            elif current_map.player_location == current_map.key_3:
                clear_screen()
                input("\n你找到了一把钥匙！")
                current_map.key_3 = ''
                current_player.key += 1



            #trigger random events
            elif random.choice([True, False, False]) != False:
                random.choice(current_events.event_list)(current_player)

            if current_player.hp <= 0:
                input("你死了。")
                playing = False
        else:
            input("\n **无效的指令!**\n")

    else:
        while True:
            clear_screen()
            if input("再玩一次? [Y/n]  ").lower() != "n":
                game_loop()
            else:
                sys.exit()

game_loop()
