# coding=utf-8

import  os

def replaceContent(filePath, srcStr,dirStr):
    try:
        f = open (filePath, 'r+')
        # all_lines = f.readlines()
        # f.seek(0,0)
        # for line in all_lines:
        #     line = line.replace(srcStr,dirStr)
        #     f.write(line)
        content = f.read()
        content = content.decode('gbk')
        f.seek(0, 0)
        srcStr = srcStr.decode('utf-8')
        dirStr = dirStr.decode('utf-8')
        contNew = content.replace(srcStr, dirStr)
        contNew = contNew.encode('gbk')
        f.write(contNew)
        f.close()
    except Exception, e:
        print "Error: ",e
    return "You did it ! Congratulations ."

# def judge(path):
#     if os.path.exists(path) and os.path.isdir(path):
#         list = os.listdir(path)
#         print type(list[0])
#
#     if os.path.isfile(path):
#         print "this  is   a  file ."

def findFiles(dirFolder, oldStr, newStr):
    for dirpath, dirnames, filenames in os.walk(dirFolder):
        # for dir in dirnames:
        #     dirs = os.path.join(dirpath,dir)
        #     print dirs

        for file in filenames:
            files = os.path.join (dirpath,file)
            replaceContent(files, oldStr, newStr)
        return "Congratulations!"

if __name__ == '__main__':

    # judge('C:\Users\huangping02\Desktop\hh.txt')
    # judge('C:\Users\huangping02\Desktop\hosts')
    rep = findFiles('C:\Users\huangping02\Desktop\\rootpath', "褰撲綘", "123")
    print rep




