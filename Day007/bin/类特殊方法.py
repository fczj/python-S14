#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-21 下午2:56
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 类特殊方法.py
# @Software: PyCharm


class Foo(object):
    '''
    测试类
    '''

    def __init__(self):
        self.name = '1'
    def __call__(self, *args, **kwargs):
        print ('call object')
    def __getitem__(self, item):
        print ('get_item',item)


a = Foo()
print (a.__doc__)
print (Foo.__dict__)

a[5]