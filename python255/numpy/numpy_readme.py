01 ����
  import numpy
  import numpy as np
  from numpy import *
02 �鿴�汾
  import numpy
  print np.version.version # 1.5.1
  python2.5.2 + windows:  numpy-1.5.1-win32-superpack-python2.5.exe ֱ������exe�ļ�
  python3.4.  + windows:  numpy-1.10.4+mkl-cp34-none-win32     
03 ��ά����
  ����Ϊlist����tuple
    һά����
      print np.array([1,2,3,4])
      print np.array((1.2,2,3,4))
      print type(np.array((1.2,2,3,4))) #<type 'numpy.ndarray'>
      print np.array((1.2,2,3,4), dtype=np.int32) # [1 2 3 4] ##ָ����������
    ��ά����
      print np.array([[1,2],[3,4]])
    
  arange.reshape
     print np.arange(15).reshape(3,5)##�������о���
  ռλ������
    numpy.zeros  numpy.ones  numpy.eye  numpy.empty
    print np.zeros((2,2,2))
04 numpy.arange
  print np.arange(15) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
  print type(np.arange(15))#<type 'numpy.ndarray'>
  print np.arange(15).reshape(3,5)##�������о���  
05 numpy.linspace
  print np.linspace(1,3,9)# �ڴ�1��3�����Բ�ֵ����9����
06 ռλ������
  numpy.zeros��numpy.ones��numpy.eye
  print np.zeros((3,4))#0����
  print np.ones((3,4))#1����
  print np.eye(3)## ��λ����  python2.5.2 �汾�� numpy1.5.1û�и�attribute
  print np.zeros((2,2,2))
07 ��������
  a = np.zeros((2,2,2))
   print a.ndim   #�����ά��
   print a.shape  #����ÿһά�Ĵ�С
   print a.size   #�����Ԫ����
   print a.dtype  #Ԫ������
   print a.itemsize  #ÿ��Ԫ����ռ���ֽ���