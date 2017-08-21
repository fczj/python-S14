#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-8 下午4:25
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 正則計算器.py
# @Software: PyCharm

import  re


custr = '1 - 2 * ( (60-30 +(40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

class Calculator():
    def __init__(self):
        pass

    def parse(self):
        pass

def cac(in_str):
    symbol = re.split('[^\-|^\+]',in_str)
    print (symbol)


while '(' in custr:
    custr_c = re.search(r'\([^()]+\)',custr)
    print(custr_c.group())
    cac(custr_c.group())
    custr = (re.sub(r'\([^()]+\)', '1', custr))
    print (custr)



