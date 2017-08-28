#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-28 下午3:10
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : gevent协程.py
# @Software: PyCharm

import gevent


def func1():
    print('\033[31;1m李闯在跟海涛搞...\033[0m')
    gevent.sleep(2)
    print('\033[31;1m李闯又回去跟继续跟海涛搞...\033[0m')


def func2():
    print('\033[32;1m李闯切换到了跟海龙搞...\033[0m')
    gevent.sleep(1)
    print('\033[32;1m李闯搞完了海涛，回来继续跟海龙搞...\033[0m')



gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
])


'''
按照串行的话需要3秒,协程需要2秒
如果有50个这样的程序,协程3秒而串行需要将等待时间加起来
和greenlet对比这个自动切换

======================================================
李闯在跟海涛搞...
李闯切换到了跟海龙搞...
李闯搞完了海涛，回来继续跟海龙搞...
李闯又回去跟继续跟海涛搞...
'''