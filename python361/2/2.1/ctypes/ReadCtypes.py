01. codeblocks ����c��dll  python2.5.5����
02. visual studio 2012���c��dll  python 3.4.3����


Microsoft Windows [�汾 6.1.7601]
��Ȩ���� (c) 2009 Microsoft Corporation����������Ȩ����

C:\Windows\system32>python
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (In
tel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from ctypes import *
>>> import os
>>> path = r"C:\Users\fan.yang\Documents\python343\ctypes\ConsoleApplication1.dl
l"
>>> print libtest.multiplyTest(2, 2)
  File "<stdin>", line 1
    print libtest.multiplyTest(2, 2)
                ^
SyntaxError: invalid syntax
>>> print(libtest.multiplyTest(2, 2))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'libtest' is not defined
>>> libtest = cdll.LoadLibrary(path)
>>> print(libtest.multiplyTest(2, 2))
4
>>>