#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-25 下午3:38
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 同时启动多线程.py
# @Software: PyCharm

import threading
import time

def run(n):
    print("task ",n )
    time.sleep(1)
    print("task done",n,threading.current_thread())

start_time = time.time()
for i in range(5):
    t = threading.Thread(target=run,args=("t-%s" %i ,))
    t.setDaemon(True) #把当前线程设置为守护线程
    t.start()


print("----------all threads has finished...",threading.current_thread(),threading.active_count())
print("cost:",time.time() - start_time)
