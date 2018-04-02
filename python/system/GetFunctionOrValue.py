# coding:utf-8

"""
获取类内函数

"""


class a():
    def __init__(self, info='info'):
        self.info = info

    def b(self):
        print('b' + self.info)


testa = a('no info')
b = getattr(testa, 'b')
b()
