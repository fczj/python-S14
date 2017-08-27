#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-26 下午5:33
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : 进程锁.py
# @Software: PyCharm


from multiprocessing import Process, Lock

def f( i):
    print('hello world', i)

if __name__ == '__main__':
    for num in range(10):
        Process(target=f, args=(num,)).start()