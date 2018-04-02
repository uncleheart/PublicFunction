import os

"""
遍历文件
"""

rootDir = "./"
os.chdir(rootDir)
for root, dirs, files in os.walk(rootDir):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
