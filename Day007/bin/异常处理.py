#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-21 下午5:24
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 异常处理.py
# @Software: PyCharm

while True:
    num1 = input('num1:')
    num2 = input('num2:')
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
        print (result)
    #同时捕获多个异常
    # except (KeyError,TypeError,ValueError) as e:
    #捕获所有异常
    except Exception as e:
        print ('出现异常，信息如下：')
        print (e)