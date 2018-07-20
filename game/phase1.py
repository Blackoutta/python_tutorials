
import math
import random
import sys
player_name = False
player_hp = 100
man_in_black_hp = 100

#询问玩家名称并开始冒险
while bool(player_name) == False:
    player_name = input("你好，冒险者！告诉我的你名字: ")
input("{}是吧，真是个好名字。好了，现在让我们开始冒险吧！".format(player_name))

#酒馆纷争
input("你叫{}，你是一名侠客。".format(player_name))
input("你在一个古道的小酒馆里正喝着酒，突然，一个带着兜帽的黑衣人坐到了你对面。")
input('黑衣人："想必阁下便是{}，久闻大名，可否赏脸喝一杯？" 说罢，便为你斟了一杯酒。'.format(player_name))

#选择1：是否喝酒
choice_1 = ""
while choice_1 != "1" and choice_1 != "2" and choice_1 != "3":
    choice_1 = input(
    """

    你会如何做？
    1. 一饮而尽
    2. 小斟一口
    3. 突然袭击
    请输入你的选择并按ENTER键确定:
    """
    )
if choice_1  == "1":
    input("酒里有毒，而你一饮而尽。")
    player_hp -= 100
    input("你被毒死了")
    sys.exit()
elif choice_1 == "2":
    input("你抿了一口酒，发现有毒，你拔刀而起！")
    player_hp -= 30
elif choice_1 == "3":
    input("你二话不说就对陌生人拔刀相向")

#战斗_黑衣人
input("开始战斗：{} VS 黑衣人".format(player_name))

while man_in_black_hp > 0:
    input("你的当前生命值为: {}".format(player_hp))
    battle_choice = input(
    """

    请选择动作：
    1. 攻击
    2. 询问来历
    请输入你的选择并按ENTER键确定:
    """
    )
    if battle_choice  == "1":
        player_damage = random.randrange(30)
        man_in_black_damage = random.randrange(20)
        man_in_black_hp -= player_damage
        player_hp -= man_in_black_damage
        input("你对黑衣人造成了{}点伤害。黑衣人对你造成了{}点伤害。".format(player_damage, man_in_black_damage))
    elif battle_choice == "2":
        input('黑衣人：不亏是{}，但是多说无益！'.format(player_name))
    if player_hp < 1:
        input("你在战斗中牺牲了！大侠请重新来过！")
        sys.exit()
else:
    input("黑衣人倒下了")
    input("战斗结束！你胜利了！")
