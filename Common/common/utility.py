#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-28 上午10:18
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : utility.py
# @Software: PyCharm

import time
from functools import wraps


def run_time(func):
    @wraps(func)
    def func_wrapper(*args,**kwargs):
        start = time.time()
        ret = func(*args,**kwargs)
        end = time.time()
        print('程序运行时间:')
        print (end-start)
        return ret
    return func_wrapper


