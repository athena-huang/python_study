# coding:utf-8

# 关于字典dictionary的无序
# i=0
# for i in range(4):
#     tinydict = {'name1': 'john','code':6734, 'dept': 'sales', 'name2': 'Sara','code2':1234, 'dept2': 'dev'}
#     print tinydict.keys()
#     print tinydict.values()
#     print "-------------------"

# 掷骰子的游戏，猜大小
import random
# import sys
# import time
#
# result = []
# while True:
#     result.append(int(random.uniform(1,7)))
#     result.append(int(random.uniform(1,7)))
#     result.append(int(random.uniform(1,7)))
#     print result
#     count = 0
#     index = 2
#     pointStr = ""
#     while index >= 0:
#         currPoint = result[index]
#         count += currPoint
#         index -= 1
#         pointStr += " "
#         pointStr += str(currPoint)
#     if count <= 11:
#         sys.stdout.write(pointStr + " -> " + "小" + "\n")
#         time.sleep(1)
#     else:
#         sys.stdout.write(pointStr + " -> " + "大" + "\n")
#         time.sleep(1)
#     result = []




# 剪子石头布的游戏
# while 1:
#     s = int(random.randint(1, 3))
#     if s == 1:
#         ind = "石头"
#     elif s == 2:
#         ind = "剪子"
#     elif s == 3:
#         ind = "布"
#     m = raw_input('输入 石头、剪子、布,输入"end"结束游戏:')
#     blist = ['石头', "剪子", "布"]
#     if (m not in blist) and (m != 'end'):
#         print "输入错误，请重新输入！"
#     elif (m not in blist) and (m == 'end'):
#         print "\n游戏退出中..."
#         break
#     elif m == ind :
#         print "电脑出了： " + ind + "，平局！"
#     elif (m == '石头' and ind =='剪子') or (m == '剪子' and ind =='布') or (m == '布' and ind =='石头'):
#         print "电脑出了： " + ind +"，你赢了！"
#     elif (m == '石头' and ind =='布') or (m == '剪子' and ind =='石头') or (m == '布' and ind =='剪子'):
#         print "电脑出了： " + ind +"，你输了！"

# 10-20内的质数
# for num in range (10,20):
#     for i in range (2,num):
#         if num % i == 0:
#             j=num/i
#             print "%d = %d * %d" % (num,i,j)
#             break
#     else:
#             print "%d是一个质数" %num


# 打印空心等边三角形
# rows = int(raw_input('输入行数：'))
# for i in range(0, rows):
#     for k in range(0, 2 * rows - 1):
#         if (i != rows - 1) and (k == rows - i - 1 or k == rows + i - 1):
#             print " * ",
#         elif i == rows - 1:
#             if k % 2 == 0:
#                 print " * ",
#             else:
#                 print "   ",
#         else:
#             print "   ",
#     print "\n"

# range和enumerate的区别：
# s = 'qazxswedcvfr'
# for i in range(0,len(s),2):
#     print s[i]
#
# for (index,char) in enumerate(s):
#     print "index=%d,char=%s" % (index,char)

# by 喝药剂
# coding:utf-8
# import urllib
# import json
# import os
#
# def mkdir(path):
#     path = path.strip()
#     path = path.rstrip("\\")
#     isExists = os.path.exists(path)
#     if not isExists:
#         os.makedirs(path)
#         return True
#     else:
#         return False
#
# if __name__ == '__main__':
#     imglist = []
#     # 返回一个类文件对象
#     f = urllib.urlopen("https://news-at.zhihu.com/api/4/news/latest")
#     # 类文件对象具有read（）readline() , readlines() , fileno() , close() 等方法
#     s = f.read()
#     myData=json.loads(s)
#     [imglist.append(myData['stories'][i]['images']) for i in range(len(myData['stories']))]
#     mkpath = "c:\\%s" % myData['date']
#     mkdir(mkpath)
#     [urllib.urlretrieve(imgurl[0], r'%s\%s.jpg' % (mkpath,imgurl[0].replace(r'/','-').replace('.','#').replace(':',u'：'))) for imgurl in imglist]
#


# 类  公开变量  私有变量
#
# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0  # 公开变量
#
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print self.__secretCount
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print counter.publicCount
# print counter._JustCounter__secretCount  # 报错，实例不能访问私有变量