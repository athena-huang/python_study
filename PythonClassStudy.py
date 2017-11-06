# coding:utf-8
from ZhiHuHelper import Crawler


def main():
    crawler = Crawler("https://news-at.zhihu.com/api/4/news/latest", "/data/pic")
    crawler.download()

if __name__ == '__main__':
    main()
