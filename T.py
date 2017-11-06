# coding:utf-8

# import time
# import calendar
#
# # import copy
# #
# # a = [1, 2, 3, 4, ['a', 'b']]
# #
# # b = a
# # c = copy.copy(a)
# # d = copy.deepcopy(a)
# #
# # a.append(5)
# # a[4].append('c')
# #
# # print('a = ', a)
# # print('b = ', b)
# # print('c = ', c)
# # print('d = ', d)
#
#
# print "当前时间戳：" , time.time()
#
# print "时间辍方式向时间元组转换：" , time.localtime(time.time())
#
# print "获取格式化的时间:", time.asctime( time.localtime(time.time()) )
#
# # 格式化成xxxx-xx-xx xx:xx:xx形式
# print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#
# # 格式化成Sat Mar 28 22:24:24 2016形式
# print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
#
# # 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2016"
# print "time.mktime: ", time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))
#
# # print "time.strptime: ", time.strptime(a, "%a %b %d %H:%M:%S %Y")
#
# print "##########################################################"
#
# print time.localtime(),"VS.", time.localtime(time.time())
# print time.asctime()
#
# print "##########################################################"
#
# # def procedure():
# #     time.sleep(2.5)
# #
# # # measure process time
# # t0 = time.clock()
# # procedure()
# # print time.clock() - t0, "seconds process time"
# #
# # # measure wall time
# # t0 = time.time()
# # procedure()
# # print time.time() - t0, "seconds wall time"
#
# print "##########################################################"
# print "-------------我是time与calendar的分界线-----------------------"
#
# #cal = calendar.month(2017, 7)
# #print cal
#
#
# # print time.ctime()
#
# #print calendar.calendar(2017, w=2, l=1, c=6)
# #print calendar.leapdays(1900, 2017)
# # print calendar.month(2017, 7, w=2, l=1)
# # print calendar.monthcalendar(2017, 7)
# # print calendar.monthrange(2017, 7)
# print calendar.weekday(2017, 7, 28)
#
# print "---------------------全局变量VS局部变量--------------------------------"
#
# total = 0   # 全局变量
#
# def sum1(arg1, *varargs):
#     total=0
#     for var in varargs:
#         total = total+var
#
#     total=total+arg1     #局部变量
#     return total
#
# print "函数内的total：", sum1(10,20,56,44)
# print "函数外的total：", total

# print "-------import XX VS from XX import * "
# import math
#
# print math.pi

# from math import *
#
# print pi



# info = "Adress : "
# def func_father(country):
#     def func_son(area):
#         city = "Shanghai "
#         print(info + country + city + area)
#
#     city = " Beijing "
#     func_son("ChaoYang ")
#     return city
#
# innerCity = func_father("China ")
# print innerCity


# def func1(i, str):
#     x = 12345
#     print(locals())
#
#
# func1(1, "first")


import copy
from copy import deepcopy
# gstr = "global string"
#
# def func1(i, info):
#     x = 12345
#     print(locals())
#
# func1(1, "first")
#
# if __name__ == "__main__":
#     print("the current scope's global variables:")
#     dictionary = globals()
#     print(dictionary)



# print "---------------命名空间和作用域--------------"
# Money = 2000
#
#
# def AddMoney():
#     # 想改正代码就取消以下注释:
#     global Money
#     Money = Money + 1
#
#
# print Money
# AddMoney()
# print Money

# print "-----------dir() 函数一个排好序的字符串列表,内容是一个模块里定义过所有模块，变量和函数---------------------"
# import math
#
# content = dir(math)
#
# print content;

