import random
from job_stats import *
from characters import *
from system import clear_screen

# 导入怪物实例
zombie = Zombie(zombie_stats)
fatty = Fatty(fatty_stats)
necromancer = Necromancer(necromancer_stats)




class Events:

    def __init__(self):
        self.event_list = [self.event_1, self.event_2, self.event_3]  #放入做好的事件

# Checks
    def check_hp(self, current_player, monster):
        if current_player.hp > monster.hp:
            return True
        else:
            return False

    def check_mp(self, current_player, monster):
        if current_player.mp > monster.mp:
            return True
        else:
            return False

    def check_str(self, current_player, monster):
        if current_player.str > monster.str:
            return True
        else:
            return False

    def check_dex(self, current_player, monster):
        if current_player.dex > monster.dex:
            return True
        else:
            return False

    def check_int(self, current_player, monster):
        if current_player.int > monster.int:
            return True
        else:
            return False

# Events

    def event_1(self, current_player):
        while True:
            clear_screen()
            input("一只无脑的僵尸出现在你面前...")
            input("僵尸: '人类...脑子...'")
            print("\n你会怎么做?")
            choice = input("1. 冲上去攻击它!\n2. 从它身旁绕过去\n3. 问: 1+1等于几?\n\n请选择一个选项并按回车确认:     ")
            if choice == '1':
                if self.check_str(current_player, zombie) and self.check_hp(current_player, zombie):
                    input("你打败了僵尸！")
                    break
                else:
                    damage = random.randint(10, 30)
                    input("你不敌僵尸的攻势，被他击倒在地后，慌忙逃窜.")
                    input("你的HP减少了{}!".format(damage))
                    # current_player.hp -= damage
                    current_player.hp -= damage
                    break

            elif choice == '2':
                if self.check_dex(current_player, zombie):
                    input("你迅速从僵尸身边饶了过去！")
                    break
                else:
                    damage = random.randint(15, 40)
                    input("僵尸比你想象中来得灵活，你被扑倒在地。")
                    input("在被咬了一口之后，你挣脱了出来，落荒而逃。")
                    input("你的HP减少了{}!".format(damage))
                    current_player.hp -= damage
                    break

            elif choice == '3':
                if self.check_int(current_player, zombie):
                    input("僵尸: 啊啊，等于几...1+1等于几...啊啊啊啊啊!")
                    input("僵尸的脑浆耗尽，倒在地上一动也不动了。")
                    break
                else:
                    damage = random.randint(20, 30)
                    input("僵尸: 当然是等于2!我讨厌别人把我当傻瓜!")
                    input("你被僵尸的攻击擦过，慌忙逃了出去。")
                    input("你的HP减少了{}!".format(damage))
                    current_player.hp -= damage
                    break
            else:
                input("请输入一个有效的数字！")
                continue

    def event_2(self, current_player):
        while True:
            clear_screen()
            input("一个面目猥琐的胖子出现在你的面前...")
            input("胖子: 什么人！来这里干什么！")
            print("\n你会怎么做?")
            choice = input(
            "1. 撒腿就逃\n2. 假装是新来的同伴\n3. 抄家伙开始攻击\n\n请选择一个选项并按回车确认:     ")
            if choice == '1':
                if self.check_hp(current_player, fatty):
                    damage = random.randint(5, 10)
                    input("胖子穷追不舍，但你体力充足，成功甩开了他！但...")
                    current_player.hp -= damage
                    input("你的HP减少了{}!".format(damage))
                    break
                else:
                    damage = random.randint(15, 30)
                    input("胖子意外的灵活，你摆脱不了他。一场恶战之后，你勉强战胜了他，但...")
                    input("你的HP减少了{}!".format(damage))
                    # current_player.hp -= damage
                    current_player.hp -= damage
                    break

            elif choice == '2':
                if self.check_int(current_player, fatty):
                    input("胖子: 原来是新来的那谁谁。。进去吧，老大在里边呢。")
                    break
                else:
                    damage = random.randint(20, 40)
                    input("胖子: 我不信，你肯定是冒牌的!")
                    input("你与胖子展开了一场恶战，你战胜了他，但...")
                    input("你的HP减少了{}!".format(damage))
                    current_player.hp -= damage
                    break

            elif choice == '3':
                if self.check_dex(current_player, fatty):
                    input("你与胖子展开了一场战斗。你没想到胖子竟然如此灵活，但你更胜一筹。")
                    input("你战胜了胖子。")
                    break
                else:
                    damage = random.randint(10, 25)
                    input("你没想到这个胖子竟然如此灵活，一场恶战之后，你战胜了胖子，但...")
                    input("你的HP减少了{}!".format(damage))
                    current_player.hp -= damage
                    break
            else:
                input("请输入一个有效的数字！")
                continue

    def event_3(self, current_player):
        while True:
            clear_screen()
            input("你看见一个死灵法师正在练习黑魔法...")
            input("他看起来没有什么防备...")
            print("\n你会怎么做?")
            choice = input("1. 展开偷袭\n2. 正面进攻\n\n请选择一个选项并按回车确认:     ")
            if choice == '1':
                if self.check_int(current_player, necromancer):
                    input("死灵法师早就觉察到你的到来并设下陷阱，然而你也早就看穿了这一点。")
                    input("你假装被陷阱所困，待死灵法师松懈之时，将他杀死。")
                    break
                else:
                    damage = random.randint(17, 30)
                    input("死灵法师早就觉察到你的到来并设下陷阱。一场恶战之后，你勉强战胜了他，但...")
                    input("你的HP减少了{}!".format(damage))
                    current_player.hp -= damage
                    break

            elif choice == '2':
                if self.check_hp(current_player, necromancer):
                    damage = random.randint(5, 15)
                    input("你从正面进攻死灵法师。但它忽然召唤出一群僵尸。")
                    input("费了一番力气，你战胜了死灵法师和他的爪牙，但...")
                    input("你的HP减少了{}!".format(damage))
                    current_player.hp -= damage
                    break
                else:
                    damage = random.randint(20, 40)
                    input("你从正面进攻死灵法师。但它忽然召唤出一群僵尸。")
                    input("你寡不敌众，被打得落荒而逃。")
                    input("你的HP减少了{}!".format(damage))
                    current_player.hp -= damage
                    break

            else:
                input("请输入一个有效的数字！")
                continue
