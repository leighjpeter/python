# -*- coding: utf-8 -*-
#测试多少次之后会失败
#导入随机数模块

#计算大转盘概率事件

import random
import time
import sys

wheel_list = [2, 4, 2, 7, 2, 4, 2, 12, 2, 7, 2, 4, 2, 200, 4, 2, 4, 2, 4, 2, 12, 2, 7, 2, 4, 2, 25, 2, 4, 2, 7, 2, 12, 2, 4, 2, 7, 2, 4, 2, 201, 2, 4, 2, 7, 4, 2, 12, 2, 7, 2, 4, 2, 25]


#设置一组十次的随机数，0为负，1为胜
def Ten_YiZu(answers,cishu):
    while cishu:
      x = random.choice(wheel_list)
      if x==2 or x==4:
        x = 1
      else:
        x = 0
      answers.append(x)
      cishu-=1
    return answers

#设置下注函数，参数分别为 本金，支出，随机值列表，输赢变量
def Start(benjin,zhichu,answers,win):

    for i, ans in enumerate(answers):
        zhichu_this = zhichu * (pow(4, i) * 3)
        if benjin < zhichu_this:
            win = 1
            print(answers)
            break
        #止损次数
        if i>5:
            win = 1
            print(answers)
            break
        benjin = benjin-zhichu_this
        zhichustr = str(zhichu)
        benjinstr = str(benjin)
        #if benjin < 0:
        #    win = 0
        #    print(answers)
        #    break
        if ans == 0 or benjin < 0:
            win = 0
        elif ans > 0:
            benjin = benjin + zhichu * (pow(4, i+1))
            benjinstr =str(benjin)
            win = 1
            break
        else:
            pass
    return win, benjin      #返回输赢变量

cishu = 10
benjin = 10000
zhichu = 10
xunhuancishu = 1

#answers = []
#print(Ten_YiZu(answers, cishu))

t1 = time.time()

while 1:
    answers = []
    win =1
    answers = Ten_YiZu(answers, cishu)
    a, benjin = Start(benjin,zhichu,answers,win)
    #如果赢了，pass，如果输了，输出第几次
    if win==a:
        print("您在第{0}次获胜，剩余本金为:{1}".format(xunhuancishu, benjin))
    else:
        print("您将在第{0}次亏损，剩余本金为:{1}".format(xunhuancishu, benjin))
    xunhuancishu+=1
    if benjin < zhichu * (pow(4, 0) * 3):
        print('耗时：', time.time() - t1)
        sys.exit(0)
    #time.sleep(1)
    if xunhuancishu > 10000:
        sys.exit(0)
        print('耗时：', time.time() - t1)
    #time.sleep(3)