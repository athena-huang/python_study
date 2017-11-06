# coding:utf-8
import urllib
import json
import os
# 返回一个类文件对象
f = urllib.urlopen("https://news-at.zhihu.com/api/4/news/latest")
# 类文件对象具有read（）readline() , readlines() , fileno() , close() 等方法
s = f.read()
print s

# 将已编码的 JSON 字符串解码为 Python 对象
myData=json.loads(s)
print myData

# 获取所有images的url，存入 imglist
imglist=[]
for i in range(len(myData['stories'])):
    imglist.append(myData['stories'][i]['images'])
# print imglist

# 创建以“date”中的时间命名的路径
def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False

mkpath = "c:\\%s" % myData['date']
mkdir(mkpath)
# print "mkpath=", mkpath

# 将图片下载到本地创建的路径下，路径中不能包含的特殊字符需要转换
for imgurl in imglist:
    print imgurl[0]
    urllib.urlretrieve(imgurl[0], r'%s\%s.jpg' % (mkpath,imgurl[0].replace(r'/','-').replace('.','#').replace(':',u'：')))
