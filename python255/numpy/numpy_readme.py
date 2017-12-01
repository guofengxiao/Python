01 引入
  import numpy
  import numpy as np
  from numpy import *
02 查看版本
  import numpy
  print np.version.version # 1.5.1
  python2.5.2 + windows:  numpy-1.5.1-win32-superpack-python2.5.exe 直接运行exe文件
  python3.4.  + windows:  numpy-1.10.4+mkl-cp34-none-win32     
03 多维数组
  参数为list或者tuple
    一维数组
      print np.array([1,2,3,4])
      print np.array((1.2,2,3,4))
      print type(np.array((1.2,2,3,4))) #<type 'numpy.ndarray'>
      print np.array((1.2,2,3,4), dtype=np.int32) # [1 2 3 4] ##指定数据类型
    二维数组
      print np.array([[1,2],[3,4]])
    
  arange.reshape
     print np.arange(15).reshape(3,5)##三行五列矩阵
  占位符矩阵
    numpy.zeros  numpy.ones  numpy.eye  numpy.empty
    print np.zeros((2,2,2))
04 numpy.arange
  print np.arange(15) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
  print type(np.arange(15))#<type 'numpy.ndarray'>
  print np.arange(15).reshape(3,5)##三行五列矩阵  
05 numpy.linspace
  print np.linspace(1,3,9)# 在从1到3中线性插值产生9个数
06 占位符矩阵
  numpy.zeros，numpy.ones，numpy.eye
  print np.zeros((3,4))#0矩阵
  print np.ones((3,4))#1矩阵
  print np.eye(3)## 单位矩阵  python2.5.2 版本的 numpy1.5.1没有该attribute
  print np.zeros((2,2,2))
07 数组属性
  a = np.zeros((2,2,2))
   print a.ndim   #数组的维数
   print a.shape  #数组每一维的大小
   print a.size   #数组的元素数
   print a.dtype  #元素类型
   print a.itemsize  #每个元素所占的字节数