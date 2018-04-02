# coding:utf-8
import re
import os


def Tran2Str(src):
    res = ''
    for i in src.split("\\"):
        if len(i) > 0:
            res += chr(int(i))
    return res


def ReplaceAllStr(src):
    p = re.compile(r'\\(1\d\d|2[01234]\d|25[0123456]|[1-9]\d?)')
    return p.sub(lambda m: Tran2Str(m.group(1)), src)


def ReplaceFile(filePath):
    baseFilename = os.path.basename(filePath)
    dirName = os.path.dirname(filePath)
    (shotname, extension) = os.path.splitext(baseFilename)
    outputFilePath = os.path.join(dirName, shotname + "_decode" + extension)

    with open(filePath, 'r') as fr:
        content = fr.read()
        content = ReplaceAllStr(content)

    with open(outputFilePath, 'w') as fw:
        fw.write(content)


a = "\"\\s2\\175\\183\\232\\190\\147\\229\\133\\165\\229\\174\\137\\229\\190\\189\\231\\148\\181\\228\\191\\161\\230\\137\\139\\230\\156\\186\\229\\143\\183\\231\\160\\129\""

# print re.findall(r'\".*?(\\[0-9]{1,3}).*?\"',a)

print(ReplaceAllStr(a))
# print "\\232\\175\\183\\232\\190\\147".decode('unicode-escape')
# ReplaceFile('common/util_dec.lua')
