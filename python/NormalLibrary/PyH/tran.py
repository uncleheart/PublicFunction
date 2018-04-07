# coding:utf-8

import xlrd
from pyh import *

"""
Python生成html
由于平常的pyh.py只支持Python2，这里使用的pyh.py是修改后的(items函数不同)
使用时按照如下即可，如果有自定义的标签，直接可以通过添加tags即可

下面使用的是xlsx数据读取

整体的功能是从xlsx中读取数据然后转换为html
"""


def genHtml(data):
    head = tr()
    for i in data['head']:
        head += th(i)
    head = thead(head)

    body = tbody()
    for rowValues in data['body']:
        tmp = tr(cl='')
        for i in rowValues:
            tmp += td(i, cl='center')
        body += tmp

    result = table(head, body, cl="table table-striped table-bordered table-hover dataTables-example")
    return result.render()


# xlsx 数据读取
def getXlsxData(filename, booksheet=0):
    workbook = xlrd.open_workbook(filename)
    booksheet = workbook.sheet_by_index(0)
    rowHead = booksheet.row_values(0)
    result = {}
    result['head'] = rowHead
    result['body'] = []

    for i in range(1, booksheet.nrows):
        result['body'].append(booksheet.row_values(i))
    return result


if __name__ == '__main__':
    filename = '../../files/xlsx_data.xlsx'
    data = getXlsxData(filename)
    print(genHtml(data))
