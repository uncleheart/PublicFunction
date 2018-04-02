#!/usr/bin/python
# encoding=utf-8
import re
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

"""
仅限python2 使用

"""


def htc(m):
    return chr(int(m.group(1),16))
def urldecode(url):
    rex=re.compile('%([0-9a-hA-H][0-9a-hA-H])',re.M)
    return rex.sub(htc,url)


class TestHTTPHandle(BaseHTTPRequestHandler):
    def do_GET(self):

        buf = 'It works'
        self.protocal_version = "HTTP/1.1"

        self.send_response(200)

        self.send_header("Welcome", "Contect")

        self.end_headers()

        self.wfile.write(buf)
    def do_POST(self):

        buf = '已成功'
        self.protocal_version = "HTTP/1.1"

        self.send_response(200)

        self.send_header("Welcome", "Contect")

        self.end_headers()

        self.wfile.write(buf)

        length = int(self.headers.getheader('content-length'))
        qs = self.rfile.read(length)
        url = urldecode(qs)
        print("points "+url)


def start_server(serverAddress):
    http_server = HTTPServer(serverAddress, TestHTTPHandle)
    http_server.serve_forever() #设置一直监听并接收请求
    #----------------------------------------------------------------------

if __name__ == '__main__':
    serverAddress = ('0.0.0.0', 8002)

    start_server(serverAddress)