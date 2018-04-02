#coding:utf-8
import time
from functools import wraps

"""
仅限python2使用
python3使用以下代码
from timeit import timeit
from timeit import repeat
def test3(n):
    time.sleep(n)
t=timeit('test3(0.5)','from __main__ import test3',number=2)
print(t)
t=repeat('test3(0.5)','from __main__ import test3',number=2,repeat=3)
print(t)
print(min(t))

"""


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print(" %s :%s seconds" % (function.func_name, str(t1 - t0)))
        return result

    return function_timer


def fn_timer_plus(info='cost'):
    def fn_timer(function):
        @wraps(function)
        def function_timer(*args, **kwargs):
            t0 = time.time()
            result = function(*args, **kwargs)
            t1 = time.time()
            print(" %s %s :%s seconds" % (function.func_name, info, str(t1 - t0)))
            return result

        return function_timer

    return fn_timer


@fn_timer
def test1(n):
    time.sleep(n)


@fn_timer_plus(info='cost')
def test2(n):
    time.sleep(n)


if __name__ == "__main__":
    test1(1)
    test2(1.5)
