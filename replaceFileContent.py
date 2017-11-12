# coding=utf-8

# Date: 2017/11/07
# Author : Athena_Huang
# Description : replace the content particularly in file or folder

import sys
#import chardet

def replaceContent(filePath, srcStr,dirStr):
    try:
        f = open (filePath, 'r+',)
        # all_lines = f.readlines()
        # all_lines = all_lines
        content = f.read()
        content = content.decode('gbk')
        f.seek(0,0)
        srcStr = srcStr.decode('utf-8')
        dirStr = dirStr.decode('utf-8')
        contNew = content.replace(srcStr,dirStr)
        contNew = contNew.encode('gbk')
        f.write(contNew)
        # for line in all_lines:
        #     # line = line.decode('gbk')
        #     # print line
        #     # print type(line)
        #     line = line.replace(srcStr,dirStr)
        #     print "ok!"
        #     #print line.decode('gbk')
        #     f.write(line)
        f.close()

    except Exception, e:
        print "Error:",e
        print "Fail!"



if __name__ == '__main__':
    # if len(sys.argv)<4:
    #     print "Need 3 params."
    #     sys.exit(1)
    # file_name = sys.argv[1]
    # old_str = sys.argv[2]
    # new_str = sys.argv[3]

    rep = replaceContent('C:\Users\huangping02\Desktop\hh.txt', "当你", "黄萍")
    print rep


