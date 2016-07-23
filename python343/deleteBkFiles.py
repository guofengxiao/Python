# coding=utf-8
# ===================================================
# 功能：删除文件
# 删除vc保存的后缀名为包含bk的备份文件
# 添加记录日志存储
# ===================================================

# 问题
# 1. nodepad++ F5 运行一闪而过
import os
import logging
import logging.handlers
from tkinter import *
from tkinter import ttk # 必须这样引用 ? 
import tkinter as tk
from tkinter import filedialog

LOG_FILE = 'deleteBkFiles.log'

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler  最多备份5个日志文件，每个日志文件最大1M 
fmt = '%(asctime)s - %(message)s'  # 日志格式

#processPath = os.getcwd()
#processPath = r"C:\Users\fan.yang\Desktop"
#processPath = r"F:\F.Y\05 一路\20140616- 南京中科川思特（南京）\02 项目\005 运动控制\06 远荣喷涂\03 Vcm"
#deleteSuffix = "bk" # 匹配后缀名


formatter = logging.Formatter(fmt)   # 实例化formatter  
handler.setFormatter(formatter)      # 为handler添加formatter  
  
logger = logging.getLogger('deleteBkFiles')    # 获取名为tst的logger    ogging.getLogger(name)获取logger对象
logger.addHandler(handler)           # 为logger添加handler  
logger.setLevel(logging.DEBUG)




def deleteFiles(processPath,deleteSuffix):
    deleteNum = 0
    deleteSuffix = c2.get()
    for file in os.listdir( processPath ):
        if deleteSuffix in os.path.splitext(file)[1]:
            fileAbsolutePath = processPath + '\\' + file 
            os.remove( fileAbsolutePath ) # 删除路径需要用绝对路径
            deleteNum += 1
    print("delete file numbers: %d"%deleteNum)
    s = "%s"%processPath +"  ||  " +"delete file numbers: %d"%deleteNum
    logger.debug(s) 


# 路径选择事件
def button1Evn():
    
    file_dir = filedialog.askdirectory(initialdir = r"C:\Users\fan.yang\Desktop") # 默认选择桌面路径
    e1.insert(0,file_dir)

def deleteEvn():
    processPath = e1.get()
    deleteSuffix = c2.get()
    deleteFiles(processPath,deleteSuffix)

root = tk.Tk()
root.title("Delete The Suffix Files") # 设置GUI 标题
Label(root,text = "File Path:").grid(row = 0,sticky = W) # sticky 左对齐
e1 = Entry(root,width = 30)
e1.grid(row = 0,column = 1,sticky = W)
button1 = Button(root,text = "Select Path",width = 10,command = button1Evn)
button1.grid(row = 0,column = 2,sticky = W)


Label(root,text = "Suffix Path:").grid(row = 1, sticky = W)
c2 = ttk.Combobox(root,width = 27,values = ["bk","png","vcm"])
c2.current(0)
c2.grid(row = 1,column = 1,sticky = W)
button2 = Button(root,text = "Delete",width = 10,command = deleteEvn)
button2.grid(row = 1,column = 2,sticky = W)


root.mainloop()

