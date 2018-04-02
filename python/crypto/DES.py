# coding:utf-8
import pyDes
import base64
import urllib

"""
仅限python2
"""

pydes = pyDes.des("scm%e458", pyDes.CBC, '\x01\x02\x03\x04\x05\x06\x07\x08', pad=None, padmode=pyDes.PAD_PKCS5)


def encrypt(data):
    return base64.b64encode(pydes.encrypt(data.encode()))


def decrypt(data):
    return pydes.decrypt(base64.b64decode(data))


m = 'test'
c = encrypt(m)
print(c)
dc = urllib.unquote(c)
print(decrypt(dc))
