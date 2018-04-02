# coding:utf-8
import argparse
import os
import re
import shutil

'''
获取linux 下可执行文件依赖的动态链接库
可以设置为指定目录下的动态链接库

之后可以加上windows，使用方法为在powershell下运行
Start-Process -PassThru calc.exe | Get-Process -Module
得到如下结果
   Size(K) ModuleName                                         FileName
   ------- ----------                                         --------
        44 calc.exe                                           C:\Windows\system32\calc.exe
      1920 ntdll.dll                                          C:\Windows\SYSTEM32\ntdll.dll
       696 KERNEL32.DLL                                       C:\Windows\System32\KERNEL32.DLL
      2456 KERNELBASE.dll                                     C:\Windows\System32\KERNELBASE.dll
     20696 SHELL32.dll                                        C:\Windows\System32\SHELL32.dll
       628 msvcrt.dll                                         C:\Windows\System32\msvcrt.dll

'''


def run_ldd(inputFile):
    inputFile = os.path.abspath(inputFile)
    result = os.popen('ldd %s' % (inputFile)).read()
    # result='''	linux-vdso.so.1 =>  (0x00007fff981c4000)
    # libQt5Core.so.5 => /home/uncleheart/Qt5.6.3/5.6.3/gcc_64/lib/libQt5Core.so.5 (0x00007f2b78aed000)
    # libicui18n.so.56 => /home/uncleheart/Qt5.6.3/5.6.3/gcc_64/lib/libicui18n.so.56 (0x00007f2b78640000)
    # libicuuc.so.56 => /home/uncleheart/Qt5.6.3/5.6.3/gcc_64/lib/libicuuc.so.56 (0x00007f2b78288000)
    # libicudata.so.56 => /home/uncleheart/Qt5.6.3/5.6.3/gcc_64/lib/libicudata.so.56 (0x00007f2b768a5000)

    return result


p = re.compile('\s*(.+?) \=\>\s+?([^\s]+?)\s+?\(0x')


def getMap(data):
    global p
    data = p.findall(data)
    print(data)
    # data = re.findall('\s*(.+?) \=\>\s+?([^\s]+?)\s+?\(0x',data)
    return data


def copyFile(data, preDir, outputDir, debug=False):
    for (name, path) in data:
        if path.startswith(preDir):
            filename = os.path.split(path)[1]
            newPath = os.path.join(outputDir, filename)
            shutil.copyfile(path, newPath)
            if debug:
                print(path, newPath)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input_file',
        type=str,
        required=True,
        help='输入文件路径',
    )
    parser.add_argument(
        '--output_dir',
        type=str,
        default='./',
        help='存放动态链接库的路径'
    )
    parser.add_argument(
        '--lib_pre_dir',
        type=str,
        default='/home/uncleheart/Qt5.6.3',
        help='要进行复制的动态链接库路径前缀'
    )
    parser.add_argument(
        '--debug',
        type=bool,
        default=False,
        help='debug?'
    )
    FLAGS, unparsed = parser.parse_known_args()
    data = run_ldd(FLAGS.input_file)
    if FLAGS.debug:
        print(data)

    mapData = getMap(data)
    copyFile(mapData, FLAGS.lib_pre_dir, FLAGS.output_dir)
