#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-26 下午3:45
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : 进程基础使用.py
# @Software: PyCharm


from multiprocessing import Process
import time
import os


def f(name):
    print('pid{}'.format(os.getpid()))          #获取进程号
    print('ppid{}'.format(os.getppid()))        #获取父进程号
    time.sleep(10)
    print('hello', name)


if __name__ == '__main__':
    print (os.getpid())
    p = Process(target=f, args=('bob',))
    p1 = Process(target=f, args=('bobs',))
    p.start()
    p1.start()
    p.join()
    p1.join()