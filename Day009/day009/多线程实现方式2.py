#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-25 下午3:32
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 多线程实现方式2.py
# @Software: PyCharm

import threading
import time


class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):#定义每个线程要运行的函数

        print("running on number:%s" %self.num)

        time.sleep(3)

if __name__ == '__main__':

    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()

