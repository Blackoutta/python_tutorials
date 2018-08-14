import system_feature
import characters
import random

def battle(name, hp, atk):
    input("你遇到了一只凶猛的{}!".format(name))
    system_feature.clear_screen()
    while True:
        system_feature.clear_screen()
        print("你的当前HP: {}".format(characters.player_hp))
        print("{}的当前HP: {}\n".format(name, hp))
        input("回合开始!")
        monster_dmg = atk + random.randint(0,5)
        characters.player_hp -= monster_dmg
        input("{}对你造成了{}点伤害！".format(name, monster_dmg))

        player_dmg = characters.player_atk + random.randint(0,5)
        hp -= player_dmg
        input("你对{}造成了{}点伤害！".format(name, player_dmg))

        if characters.player_hp < 0:
            input("你被{}杀死了!".format(name))
            input("GAME OVER")
            break
        if hp < 0:
            input("你杀死了{}!".format(name))
            break


def event_1(name, hp, atk):
    input("一个{}挡住了你的去路...".format(name))
    while True:
        print("\n{}: 告诉我，你最喜欢的推理小说是哪本？".format(name))
        choice = input("""
    ------------------------------------
        1. 解忧杂货店
        2. 姑获鸟之夏
        3. 魍魉之夏
    ------------------------------------

>>>输入1 - 3 并按回车键确定:  """
        )
        system_feature.clear_screen()
        if choice == "1":
            input("{}: 啊...我看到了...一段穿越时空的羁绊，一首小人物的自我救赎之歌。".format(name))
            input("{}: 你是一个善良的人，冒险者。".format(name))
            heal = random.randint(1,20)
            input("{}为你恢复了{}点生命值!".format(name, heal))
            characters.player_hp += heal
            break
        elif choice == "2":
            input("{}: 啊...我看到了...三重灵魂的纠葛。".format(name))
            input("{}: 你是一个坚强的人，冒险者。".format(name))
            heal_mana = random.randint(1,20)
            input("{}为你恢复了{}点法力值!".format(name, heal_mana))
            characters.player_mana += heal_mana
            break
        elif choice == "3":
            input("{}: 啊...我看到了...匣中少女和伴随其而来的魍魉！".format(name))
            input("{}: 冒险者！我讨厌箱子！".format(name))
            input("{}向你发起进攻！".format(name))
            battle(name, hp, atk)
            break


def event_2(name, hp, atk):
    input("Test if event 2 is working.")

def event_3(name, hp, atk):
    input("Test if event 3 is working.")

def event_4(name, hp, atk):
    input("Test if event 4 is working.")


# if __name__ == "__main__":
# random_monster = characters.monster_ls.pop(random.randint(0, len(characters.monster_ls) -1))

event_ls = [
event_1,
event_2,
event_3,
event_4]
