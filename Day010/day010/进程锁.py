#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-26 下午5:33
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : 进程锁.py
# @Software: PyCharm


from multiprocessing import Process, Lock
import time

def f( i,lock):
    #相当于是串行了
    lock.acquire()
    print('hello world', i)
    time.sleep(1)
    print('*'*i)
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    for num in range(10):
        Process(target=f, args=(num,lock,)).start()

#屏幕属于公共的资源,在使用前加锁
#python3输出是对的
