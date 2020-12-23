# coding=utf-8
# ============================================
# 功能：
# 比如 
# 执行程序后 名字为 
# 操作管理
# ============================================

import os
import re
import sys
import tkinter
from distutils.core import setup
# 更名文件类型
FILETYPES = [".xlsx",".xls"]

#更名顺序
NUMBERFIRST = False

#运行目录
CurrentPath = os.getcwd()
#当前脚本目录
#print(sys.argv[0])
ScriptPath = os.path.split(os.path.realpath(sys.argv[0]))[0]
#print(ScriptPath)

def ReNameFun(flag):
    for file in os.listdir(ScriptPath):
        fileType = os.path.splitext(file)[-1]
        if fileType in FILETYPES:
            oldDir = os.path.join(ScriptPath,file)# 之前
            fileName = os.path.splitext(file)[0]
            #print(file)
            #正则表达式: [\u4e00-\u9fa5], 只匹配汉字
            #依据汉字的Unicode码表: 从u4e00~u9fa5, 即代表了符合汉字GB18030规范的字符集
            #ChineseChar = ''.join(re.findall('[\u4e00-\u9fa5]',fileName))
            Number = ''.join(re.findall('[0-9]',fileName))
            NotNumber = ''.join(re.findall('[^0-9]',fileName))
            #print(Number)
            #print(NotNumber)
            if flag == True:
                newFileNmae = ScriptPath + '\\'  +Number +  NotNumber  + fileType
            elif flag == False:
                newFileNmae = ScriptPath + '\\' +NotNumber +  Number  + fileType
                #print(newFileNmae)
            else:
                pass
            try:
                os.rename(oldDir,newFileNmae)
            except:
                assert("rename error!") 

top = tkinter.Tk()

# 注意：使用lambda 才能传参数
B1 = tkinter.Button(top, text ="数字优先", command = lambda :ReNameFun(True))
B2 = tkinter.Button(top, text ="字符优先", command = lambda :ReNameFun(False))
B1.pack()
B2.pack()



top.mainloop()


