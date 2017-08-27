#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-26 下午4:50
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : 进程通信1.py
# @Software: PyCharm


from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()