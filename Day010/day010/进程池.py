#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-26 下午5:50
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : 进程池.py
# @Software: PyCharm


from  multiprocessing import Process,Pool
import time

def Foo(i):
    time.sleep(2)
    return i+100

def Bar(arg):
    print('-->exec done:',arg)

pool = Pool(5)

for i in range(10):
    pool.apply_async(func=Foo, args=(i,),callback=Bar)
    #pool.apply(func=Foo, args=(i,))

print('end')
pool.close()
pool.join()#进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。