#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-26 上午11:40
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : 队列.py
# @Software: PyCharm


import queue

q = queue.Queue()

q.put('a')
q.put('b')
q.put('c')
q.put('d')

print(q.get())
print(q.get())
print(q.get())
print(q.get())