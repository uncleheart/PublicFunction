# coding:utf-8
import logging
from datetime import datetime
import os
import sys


class LogModule():
    """
    在入口函数内进行调用 LogModule.init()
    使用方法
        import LogModule
        LogModule.init()
    其他文件就只import logging
    并且，在使用前不能打印任何日志，即LogModule.init() 必须在最前被执行。

    默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
    日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。

    正常情况下使用以下方法打印错误
    logging.error('error')
    logging.excepiton('error')

    在python3下：
    logging.exception() 如果没有except（标准错误输出），那么将不会打印至文件中，即只有在有错误输出时，exception才在日志文件中起作用
    故logging.error()是打印错误信息，exception()是打印错误输出，并且添加自定义的错误。

    """
    name = 'name'
    base_dir = os.path.dirname(sys.argv[0])
    pre_dir = 'logs'
    filename = "%s-%s.log" % (name, datetime.now().strftime("%Y-%m-%d-%H%M%S"))
    file_path = os.path.join(base_dir, pre_dir, filename)

    def get_filepath():
        return LogModule.file_path

    def set_filepath(name, base_dir, pre_dir, filename, file_path):
        if None != name:
            LogModule.name = name
            LogModule.filename = "%s-%s.log" % (name, datetime.now().strftime("%Y-%m-%d"))
        if None != base_dir:
            LogModule.base_dir = base_dir
        if None != pre_dir:
            LogModule.pre_dir = pre_dir
        if None != filename:
            LogModule.filename = filename
        if None != file_path:
            LogModule.file_path = file_path
        else:
            LogModule.file_path = os.path.join(LogModule.base_dir, LogModule.pre_dir, LogModule.filename)

    def init():
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=LogModule.file_path,
                            filemode='w')
        # 下面是设置什么时候打印到屏幕上
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)


def init():
    LogModule.init()


def set_filepath(
        name=None,
        base_dir=None,
        pre_dir=None,
        filename=None,
        file_path=None):
    LogModule.set_filepath(name, base_dir, pre_dir, filename, file_path)


if __name__ == '__main__':
    LogModule.init()
    logging.critical('test')
    logging.error('test')
    logging.warning('test')
    logging.info("test")
    logging.debug('test')
    logging.exception('test')
