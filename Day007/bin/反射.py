#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-21 下午4:13
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 反射.py
# @Software: PyCharm


class Web():
    def login(self):
        print ('login')
    def url(self):
        print ('access url')
def run():
    web = Web()
    inp = input('http://')
    if hasattr(web,inp):
        func = getattr(web,inp)
        func()
    else:
        print ('404')

def out_pri():
    return ('1234')


if __name__ == "__main__":
    setattr(Web, 'out_pri', out_pri)
    print(Web.out_pri())
    run()