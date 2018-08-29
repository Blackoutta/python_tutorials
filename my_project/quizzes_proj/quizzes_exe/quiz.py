from library import *
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Quiz():

    def __init__(self, library):
        for key, value in library.items():
            setattr(self, key, value)
        self.correct_count = 0

    def start_quiz(self):
        clear_screen()
        self.answer_ls_cp = list(self.answer_ls)
        self.output_ls = []
        self.answer_num = len(self.answer_ls)
        while True:
            clear_screen()
            print("\n** {}:\n".format(self.question))

            for i in range(self.answer_num):
                self.answer_num -= 1
                self.rand_answer = self.answer_ls_cp.pop(random.randint(0, self.answer_num))
                self.output_ls.append(self.rand_answer)

            for i in self.output_ls:
                print("{} - {}".format(self.output_ls.index(i) + 1, i))

            self.correct_answer_index = self.output_ls.index(self.real_answer)


            try:
                self.choice = int(input("\n请输入答案的编号并按回车确认: "))
            except ValueError:
                input("\n** 必须输入一个有效数字！**")
                continue
            if self.choice == self.correct_answer_index + 1:
                input("\n恭喜你，答对了！O(∩_∩)O")
                return 1

            elif self.choice not in list(range(1, len(self.output_ls) + 1)):
                input("\n** 必须输入一个有效数字！**")

            else:
                input("\n回答错误！(•́へ•́╬)")
                return 0




#这里设置课题  <<<<<<<<<<<<<<<<<<<
subject = "Python课程简介"

def quiz_loop():
    clear_screen()
    input("欢迎答题!\n\n本次的主题为: 《{}》".format(subject))
    correct_count = 0

    #在这里通过class导入题目并创建实例  <<<<<<<<<<<<<<<<<<<
    q1 = Quiz(quiz_1)
    q2 = Quiz(quiz_2)
    q3 = Quiz(quiz_3)
    q4 = Quiz(quiz_4)
    q5 = Quiz(quiz_5)
    q6 = Quiz(quiz_6)
    q7 = Quiz(quiz_7)

    #在这里把实例加入到一个列表中，用于从中随机抽取题目  <<<<<<<<<<<<<<<<<<<
    quiz_list = [q1, q2, q3, q4, q5, q6, q7]

    quiz_num = len(quiz_list)

    while len(quiz_list) != 0:
        rand_quiz = quiz_list.pop(random.randint(0, len(quiz_list) - 1))
        correct_count += rand_quiz.start_quiz()
    else:
        clear_screen()
        print("你一共答对了{}/{}道题目！".format(correct_count, quiz_num))
        if correct_count == quiz_num:
            rating = "天秀"
        elif correct_count / quiz_num > 0.7:
            rating = "优秀"
        elif correct_count / quiz_num > 0.3:
            rating = "一般秀"
        else:
            rating = "再接再厉秀"
        print("\n你的评价是: ** {} **".format(rating))
        again = input("\n再试一次? Y/N:  ")
        if again.lower() != "n":
            quiz_loop()
quiz_loop()
