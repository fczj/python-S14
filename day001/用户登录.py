#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Time    : 17-8-3 下午5:37
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 002.py
# @Software: PyCharm

'''
=================================================================
1.用户登录程序
2.允许输入错误的用户名和密码三次
2.密码错误三次后锁定
3.锁定的用户不能登录
=================================================================
'''

import os
import sys
class UserInfo():
    def __init__(self,name):
        self.name = name
        self.info = {}
        self.user_dict()
    def user_dict(self):
        with open('./user','r') as f:
            for line in f.readlines():
                user,password,status= line.strip().split(':')
                self.info[user] = {}
                self.info[user]['password'] = password
                self.info[user]['status'] = status

    def has_user(self):
        if self.name in self.info:
            return True
        return False

    def is_lock(self):
        if self.info[self.name]['status'] == 'lock':
            return True
        return False

    def auth_password(self,password):
        if self.info[self.name]['password'] == password:
            return True
        return False

    def update_status(self):
        self.info[self.name]['status'] = 'lock'

    def save_info(self):
        os.remove('./user')
        for k,v in self.info.items():
            with open('./user','a') as f:
                f.write('{}:{}:{}\n'.format(k,v['password'],v['status']))

class Login():
    def __init__(self):
        pass
    def set_name(self):
        self.name = input('input username:')
    def set_password(self):
        self.password = input('input password:')


if __name__ == "__main__":
    login = Login()
    i = 1
    while i < 4:
        login.set_name()
        info = UserInfo(login.name)
        if info.has_user():
            if info.is_lock():
                print ('用户{}已经被锁定,请联系管理员'.format(login.name))
                sys.exit()
            break
        else:
            print ('用户{}不存在请重新输入'.format(login.name))
        i += 1
    else:
        print('输入用户名错误超过三次,登录失败')
        sys.exit()

    i = 1
    while i < 4:
        login.set_password()
        if info.auth_password(login.password):
            print ('登录成功')
            break
        else:
            print ('{}用户密码不正确,请重输入'.format(login.name))
        i += 1
    else:
        print('密码输出错误超过三次')
        info.update_status()
        info.save_info()
