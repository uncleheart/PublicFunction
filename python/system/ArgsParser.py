#!/usr/bin/python
#coding:utf-8
from argparse import ArgumentParser

"""
用于解析输入参数
"""

if __name__ == '__main__':

    p = ArgumentParser(usage='it is usage tip', description='this is a test')
    p.add_argument('-o','--one', default=1, type=int, help='the first argument')
    p.add_argument('-t','--two', default=2, type=int, help='thesecondargument')
    p.add_argument('-d','--docs-dir', required=True, help='documentdirectory')

    args = p.parse_args()
    # 可以打印出来查看
    print(args)

    # 打印某一个参数
    print(args.one)
    print(args.docs_dir)