#!/usr/bin/python
# coding:utf-8
import ctypes
from ctypes import *
import os

"""
使用ctypes直接调用动态链接库，没测试过python3
"""

# 参数为生成的.so文件所在的绝对路径
libtest = ctypes.cdll.LoadLibrary(os.getcwd() + '/linuxany.so')
# 如果参数是char* 或者int  可以直接调用
print(libtest.display('Hello,I am linuxany.com'))

# 如果参数是其他类型，先设置参数类型，在申请好空间传参调用
myGetData = libtest.getData
pData = ctypes.POINTER(ctypes.c_ubyte)
myGetData.argtypes = [pData]
buffersize = 1024 * 1024 * 20
# 这个是申请空间
data = (buffersize * ctypes.c_ubyte)()
# 完成调用
myGetData(data)

print(type(data))
print(data[0])
# 类型转换
strData = string_at(data, buffersize)
print(len(strData))
