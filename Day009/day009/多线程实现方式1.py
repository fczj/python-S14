#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-25 下午3:26
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 多线程实现方式1.py
# @Software: PyCharm

import time
import threading


def sayhi(name):
    print ('hi '+str(name))
    time.sleep(2)


if __name__ == "__main__":
    t1 = threading.Thread(target=sayhi,args=('bob',))
    t2 = threading.Thread(target=sayhi,args=('alex',))

    t1.start()
    t2.start()
    print(t1.getName())
    print(t2.getName())
