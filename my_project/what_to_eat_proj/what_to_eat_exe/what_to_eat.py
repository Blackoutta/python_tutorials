from dish_list import *
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



def program_loop():
    clear_screen()
    meal_ls = list(meal)
    vege_ls = list(vegetable)
    soup_ls = list(soup)
    extra_ls = list(extra)

    random_meal = meal_ls.pop(random.randint(0, len(meal_ls) - 1))
    random_vege = vege_ls.pop(random.randint(0, len(vege_ls) - 1))
    random_soup = soup_ls.pop(random.randint(0, len(soup_ls) - 1))
    random_extra = random.sample(meal_ls + vege_ls + extra_ls, 2)

    input("还在烦恼今天吃什么吗？按任意键得到一份推荐菜单！")
    print("\n今日推荐:")
    print("\n肉类: {}".format(random_meal))
    print("\n蔬菜类: {}".format(random_vege))
    print("\n汤类: {}".format(random_soup))
    print("\n随机配菜: {}, {}".format(random_extra[0], random_extra[1]))
    print("\n再次生成请按回车，输入 'q' 并按回车退出程序。")
    if input("\n>>  ").lower() != "q":
        program_loop()

program_loop()
