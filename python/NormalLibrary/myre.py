# coding:utf-8
import re

"""
等待完善，python 正则库使用
"""

a = '''
var token = 'bmxOTFUzRUEGGBEGZAM3LRc6PQkAYB8eOwocDmJHcGw0NicmJXhzJQ==';    ----重要
var count
'''

p = re.compile(r'var\stoken\s=\s\'(\S+)\';')
reRes = p.findall(a)
print(reRes)

