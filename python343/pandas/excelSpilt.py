#-*- coding : utf-8 -*-
# coding: utf-8
import pandas as pd
import os
import sys
import xlrd


CUTNAME = "楼栋"


ScriptPath = os.path.split(os.path.realpath(sys.argv[0]))[0]
filePath = ScriptPath + '\\家属区所有住户登记明细表(1)(1).xlsx'
print(filePath)
content = xlrd.open_workbook(filename=filePath,encoding_override='gb18030')


excel = pd.read_excel(content,engine='xlrd')
row_num ,column_num = excel.shape
print("行：%d"%row_num)
print("列：%d"%column_num)
print(excel)
class_list = list(excel[CUTNAME].drop_duplicates())
print(class_list)
for i in class_list:
    iris1 = excel[excel[CUTNAME]==i]
    iris1.to_excel('./output/%s.xlsx'%(i))