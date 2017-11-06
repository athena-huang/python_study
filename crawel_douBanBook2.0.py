# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import re

# link of pages
def getNewPage(url, total_page):
    page_group = []
    for i in range(1, total_page+1):
        startNum = (i-1)*25
        link = re.sub('start=(\d+)', 'start=%d' % startNum, url)
        page_group.append(link)
    return page_group

# get the html
def getHtml (url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

if __name__ == '__main__':
    url = "https://www.douban.com/doulist/1264675/?start=0"
    all_links = getNewPage(url,19)
    with open('C:\\Users\\Athena\\Desktop\\book2.txt', 'w') as f:
        for link in all_links:
            html = getHtml(link)
            soup = BeautifulSoup(html, "html.parser")
            for divs in soup.find_all('div', class_='title'):
                for each in divs:
                    if each != "\n":
                        for book in each:
                            book = book.strip()
                            bookName = book.encode('utf-8')
                            bookName = bookName.strip()
                            #print bookName
                            f.write(bookName + "\n")
            print "done"
        f.close()
