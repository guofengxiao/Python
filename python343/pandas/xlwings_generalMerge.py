#!/usr/bin/python
# -*- coding: UTF-8 -*-

#目前手动创建当天汇总表
#在17:00手动更新wechatMessage.txt
#单独发的 不标背景颜色
#Todo 数据项背景颜色还没有归0
# xls 打开报错。 政法学院表格如果需要修复 中途报错
# Todo 改成通用的表格数据合并

import xlwings as xw
import os
import time

weChatFilesPath = r"C:\Users\Administrator\Documents\WeChat Files\wxid_9wrukigt5dp322\FileStorage\File\2021-03"
wb = xw.Book(r"C:\Users\Administrator\Desktop\2021年疫情数据填报\20210304汇总\2021年春季返校相关工作统计表_汇总.xlsx")
filename = r"C:/Users/Administrator/Desktop/2021年疫情数据填报/wechatMessage.txt"
messageExlPath = r"E:\fan.yang\githubLocal\Python\Python\python343\wechatDemo\messages.xlsx"
messageExlsht1 = xw.Book(messageExlPath).sheets["sheet1"]


sht1 = wb.sheets["sheet1"]
sht2 = wb.sheets["sheet2"]
sht3 = wb.sheets["sheet3"]
'''
#获取Excel 行数和列数
nrows = sht1.used_range.last_cell.row
ncols = sht1.used_range.last_cell.column
print("nrows:%d"%nrows)
print("ncols:%d"%ncols)
print(list(range(nrows)))#将对象转换成一个列表
for i in range(nrows):#python3 中range() 返回的是一个可迭代对象
    if sht1.range('A'+str(i+1)).color == None:
        print( sht1.range('A'+str(i+1)).value )
quit()
sht1.range('A1:CF44').color = None# 刚开始恢复空白状态
#quit()
'''
sht1.range('A1:P44').color = None# 刚开始恢复空白状态 一般情形下 整个区域变化
dpa = sht2.range('A2:A43').value
person = sht2.range('B2:B43').value
dpaNames = sht3.range('A2:A43').value
#dpa_person = [ [a,b] for a,b in zip(dpa,person)] #合并成列表
person_dpa = dict(zip(person,dpa))#合并成字典
dpa_person = dict(zip(dpa,person))

table = []
for i in range(4,46,1):
    table.append("A"+ str(i))
print(table)
print(person_dpa)
print(dpaNames)
'''
for Names in dpaNames:
    print(Names.split(","))
'''

table_person = dict(zip(person,table))#合并成字典
dpa_table = dict(zip(dpa,table))#合并成字典
print(table_person)
print(dpa_table)

def text_read(filename):
# Try to read a txt file and return a list.Return [] if there was a mistake.
    try:
        file = open(filename,'r',encoding='UTF-8')
    except IOError:
        pass
    content = file.readlines()
    
    return content  
t = time.gmtime()
today = []
print('年：',t.tm_year)
print('月：',t.tm_mon)
print('日：',t.tm_mday)
print('年：',type(t.tm_year))
today.append( str(t.tm_year)+str(t.tm_mon)+str(t.tm_mday) )
today.append( str(t.tm_year)+"年"+str(t.tm_mon)+"月"+str(t.tm_mday)+"日" )
if t.tm_mon < 10 and t.tm_mday < 10:
    today.append( str(t.tm_year)+"年"+"0"+str(t.tm_mon)+"月"+"0"+str(t.tm_mday)+"日" )
    today.append( str(t.tm_year)+"0"+str(t.tm_mon)+"0"+str(t.tm_mday))
elif t.tm_mon < 10 :
    today.append( str(t.tm_year)+"年"+"0"+str(t.tm_mon)+"月"+str(t.tm_mday)+"日" )
    today.append( str(t.tm_year)+"0"+str(t.tm_mon)+str(t.tm_mday))
elif t.tm_mday < 10 :
    today.append( str(t.tm_year)+"年"+str(t.tm_mon)+"月"+"0"+str(t.tm_mday)+"日" )
    today.append( str(t.tm_year)+str(t.tm_mon)+"0"+str(t.tm_mday))

print(today)
today = []
today.append("春季返校相关工作")
print(today)
#quit()
for a,b,c in os.walk(weChatFilesPath):#a代表所在根目录;b代表根目录下所有文件夹(以列表形式存在);c代表根目录下所有文件
    for i in c:
        for day in today:
            if day in i:
                currentfilePath = weChatFilesPath + "\\" + str(i)
                dpaExl = xw.Book(currentfilePath)# 打开可能异常
                sht = dpaExl.sheets[0]
                data = sht.range('B3:P3').value #修改源数据位置
                for Names in dpaNames:
                    for name in Names.split(","):
                        if name in i:
                            print(i)
                            print(Names.split(",")[0])
                            rangeFlag = "B" + str(dpa_table[Names.split(",")[0]][1:]) + ":"+"P" + str(dpa_table[Names.split(",")[0]][1:]) #修改目标数据位置
                            sht1.range(rangeFlag).value = data
                            sht1.range(rangeFlag).color = (220,20,60)







'''
if((sht1.range('A4').color == (146, 208, 80)) and (sht1.range('A44').color == (146, 208, 80))):
    #print(sht1.range('A1:A44').color)# 默认是没有背景颜色（None）；有修改是绿色(146, 208, 80)
    sht1.range('A1:A44').color = None
'''

weChatmessageList = text_read(filename)
for i, val in enumerate(weChatmessageList):
    for (k,v) in  person_dpa.items(): 
        if k in val:
            if "无变化" in weChatmessageList[i+1] or "无数据变化" in weChatmessageList[i+1] or "没有变化" in weChatmessageList[i+1]:#未变化判断
                #print(table_person[k])
                sht1.range(table_person[k]).color = (146, 208, 80)
                #print(weChatmessageList[i+1])
            if "[文件]" in weChatmessageList[i+1]:#提交表格数据
                #print(table_person[k])
                sht1.range(table_person[k]).color = (220,20,60)
                #print(weChatmessageList[i+1])


nrows = sht1.used_range.last_cell.row
ncols = sht1.used_range.last_cell.column
print("nrows:%d"%nrows)
print("ncols:%d"%ncols)
print(list(range(nrows)))#将对象转换成一个列表
mesDict ={}
for i in range(nrows):#python3 中range() 返回的是一个可迭代对象
    if sht1.range('B'+str(i+1)).color == None:#修改 
        unsubmitDpa = sht1.range('A'+str(i+1)).value
        if dpa_person.__contains__(unsubmitDpa):
            #mesDict[dpa_person[unsubmitDpa]] = "您好，麻烦有空交一下"+ today[1] +"报表，谢谢。"
            mesDict[dpa_person[unsubmitDpa]] = "您好，麻烦有空交一下《2021年春季返校相关工作统计表》" #提示信息修改
print(mesDict)


for (k,v) in  mesDict.items(): 
    newLine = [k,v,"ToDo",None]
    lastRow = messageExlsht1.used_range.last_cell.row
    index = "A" + str(lastRow+1) + ":"+"D" + str(lastRow+1)
    messageExlsht1.range(index).value = newLine