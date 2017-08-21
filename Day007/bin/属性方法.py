#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-21 下午2:33
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 属性方法.py
# @Software: PyCharm


class Flight(object):
    def __init__(self,name):
        self.flight_name = name

    def checking_flight(self):
        print ('checking {} status'.format(self.flight_name))
        return 1

    @property
    def flight_status(self):
        if self.checking_flight() == 1:
            print  ('{} status is 1'.format(self.flight_name))

    @flight_status.setter
    def flight_status(self,status):
        print('status is {}'.format(status))

    @flight_status.deleter
    def flight_status(self):
        print('deleting')

a = Flight('hainan')
a.flight_status
a.flight_status = 5
del a.flight_status