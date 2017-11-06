# coding:utf-8

import urllib
import json
import os


class Crawler:
    def __init__(self, url, path):
        self.url = url
        self.path = path

    def mkdir(self, date):
        path = (self.path + date).rstrip("\\")
        isExists = os.path.exists(path)

        if not isExists:
            os.makedirs(path)
        return path

    def download(self):
        f = urllib.urlopen(self.url)
        s = f.read()
        myData = json.loads(s)
        imgs = []
        for i in range(len(myData['stories'])):
            imgs.append(myData['stories'][i]['images'])

        targetPath = self.mkdir(myData['date'])

        for url in imgs:
            urllib.urlretrieve(url[0], r'%s\%s.jpg' % (
                targetPath, url[0].replace(r'/', '-').replace('.', '#').replace(':', u'：')))
