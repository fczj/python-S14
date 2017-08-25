#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-25 下午5:29
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 信号量.py
# @Software: PyCharm

import threading
import  time
def run(n):
    semaphore.acquire()
    time.sleep(2)
    print("run the thread: %s\n" %n)
    semaphore.release()

if __name__ == '__main__':

    num= 0
    semaphore  = threading.BoundedSemaphore(5) #最多允许5个线程同时运行
    for i in range(22):
        t = threading.Thread(target=run,args=(i,))
        t.start()

while threading.active_count() != 1:
    pass #print threading.active_count()
else:
    print('----all threads done---')
    print(num)