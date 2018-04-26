# coding:utf-8
import sys
import threading
import time
import platform

from timeout_decorator import timeout_decorator

"""
全版本通用，并且windows与*nix都可以用，添加了一个系统版本判断。
如果是windows的情况下，则通过KThread实现
如果是其他*nix情况，则需要安装timeout_decorator
使用方法：

    这个是给定方法，确保函数执行时间不会超时
    try:
        RunTimeoutFunc(tryprint, 2, 1)
        RunTimeoutFunc(tryprint, 2, 3)
    except (timeout_decorator.TimeoutError) as e:
        print(e)

    进行执行，出现超时则会报错
    for sec in (1, 4, 5, 6):
        try:
            print('*' * 20)
            print(method_timeout(sec, 'test waiting %d seconds' % sec))
        except timeout_decorator.TimeoutError as e:
            print(e)

requirements  timeout_decorator

"""


class KThread(threading.Thread):
    """A subclass of threading.Thread, with a kill()
    method.

    Come from:
    Kill a thread in Python:
    http://mail.python.org/pipermail/python-list/2004-May/260937.html
    """

    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.killed = False

    def start(self):
        """Start the thread."""
        self.__run_backup = self.run
        self.run = self.__run  # Force the Thread to install our trace.
        threading.Thread.start(self)

    def __run(self):
        """Hacked run function, which installs the
        trace."""
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, why, arg):
        if why == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, why, arg):
        if self.killed:
            if why == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True


class TimeoutErrorPlus(timeout_decorator.TimeoutError):
    """function run timeout, 直接使用会报错，原因未知"""


def timeout(seconds):
    """超时装饰器，指定超时时间
    若被装饰的方法在指定的时间内未返回，则抛出Timeout异常"""

    def timeout_decorator_windows(func):
        """真正的装饰器"""

        def _new_func(oldfunc, result, oldfunc_args, oldfunc_kwargs):
            result.append(oldfunc(*oldfunc_args, **oldfunc_kwargs))

        def _(*args, **kwargs):
            result = []
            new_kwargs = {  # create new args for _new_func, because we want to get the func return val to result list
                'oldfunc': func,
                'result': result,
                'oldfunc_args': args,
                'oldfunc_kwargs': kwargs
            }
            thd = KThread(target=_new_func, args=(), kwargs=new_kwargs)
            thd.start()
            thd.join(seconds)
            alive = thd.isAlive()
            thd.kill()  # kill the child thread
            if alive:
                raise TimeoutErrorPlus(value='function run too long, timeout %d seconds.' % seconds)
            else:
                return result[0]

        _.__name__ = func.__name__
        _.__doc__ = func.__doc__
        return _

    sysstr = platform.system()
    if (sysstr == "Windows"):
        return timeout_decorator_windows
    else:
        import timeout_decorator
        return timeout_decorator.timeout(seconds,
                                         exception_message='function run too long, timeout %d seconds.' % seconds)


def RunTimeoutFunc(func, seconds, *args, **kwargs):
    @timeout(seconds)
    def _RunTimeoutFunc(*args, **kwargs):
        return func(*args, **kwargs)

    return _RunTimeoutFunc(*args, **kwargs)


if __name__ == '__main__':

    @timeout(5)
    def method_timeout(seconds, text):
        print('start', seconds, text)
        time.sleep(seconds)
        print('finish', seconds, text)
        return seconds


    def tryprint(x):
        print(x)
        time.sleep(x)


    try:
        RunTimeoutFunc(tryprint, 2, 1)
        RunTimeoutFunc(tryprint, 2, 3)
    except (timeout_decorator.TimeoutError) as e:
        print(e)

    for sec in (1, 4, 5, 6):
        try:
            print('*' * 20)
            print(method_timeout(sec, 'test waiting %d seconds' % sec))
        except timeout_decorator.TimeoutError as e:
            print(e)
