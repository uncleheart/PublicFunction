import execjs

source = """
function hello(a,b) {
    return a+b;
}

"""

print(execjs.compile(source).call('hello', 1, 2))
import execjs

# 执行本地的js

def get_js(filepath):
    f = open(filepath, 'r', encoding='UTF-8')
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr

jsstr = get_js("../../files/js.js")
ctx = execjs.compile(jsstr)
print(ctx.call('hello', 1, 2))
