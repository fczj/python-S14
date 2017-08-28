#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-28 下午2:54
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : grennlet协程.py
# @Software: PyCharm

from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
'''
greenlet是一个用C实现的协程模块，相比与python自带的yield，它可以使你在任意函数之间随意切换，而不需把这个函数先声明为generator
greenlet需要手动切换
结果:
12
56
34
78
'''