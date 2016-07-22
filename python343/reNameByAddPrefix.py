# coding=utf-8
# ============================================
# 功能：对后缀名.vcm 文件名前加序号操作
# 比如 A.vcm  B.vcm  C.vcm 
# 执行程序后 名字为 0001.A.vcm 0002.B.vcm 0003.C.vcm
# 目的是文件名很杂乱时，加编号使得文件名有序，方便记录
# 操作管理
# ============================================

import os
import re

def CheckName( name ):
  pattern = re.compile(r'\d{4}\.')# 01. Python原生字符串    02. 将则表达式编译成Pattern对象
  match = pattern.match( name )# 使用Pattern匹配文本，获得匹配结果
  if match == None:# 无法匹配是返回Non
    return False
  else:
    return True



existCount = 0
nonExistCount = 0
for file in os.listdir("."):# os.listdir(dirname)：列出dirname下的目录和文件  # "." 当前目录 # ".." 上一级目录
  # print( os.path.splitext(file)[1] )
  if os.path.splitext(file)[1] == ".vcm":#将path分割成目录和文件名二元组返回
    if CheckName( os.path.splitext(file)[0] ):
      existCount += 1
    else:
      nonExistCount += 1

preFixList = [str(existCount + i).zfill(4) for i in range(1,nonExistCount + 1)]

index = 0
for file in os.listdir("."):
  # print( os.path.splitext(file)[1] )
  if os.path.splitext(file)[1] == ".vcm":
    if CheckName( os.path.splitext(file)[0] ) == False:
      preFix = preFixList[index]
      filename = os.path.basename(file)
      newName = preFix + "." + filename
      try:
        os.rename(file,newName)
      except:
        assert("rename error!")
      index += 1

