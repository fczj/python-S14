#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-5 下午7:23
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : config_file.py
# @Software: PyCharm



'''
=================================================================
1.简单实现linux中sed命令
=================================================================
'''

class ConfigFile():
    def __init__(self):
        self.is_exit = False
        self.conf_file = './conf'
        self.conf_dict = {}
        pass

    def load_config(self):
        before = ''
        with open(self.conf_file,'r') as f:
            for line in f:
                if 'backend' in line:
                    print ('12341')
                    before = line.strip()
                if 'server' in line:
                    self.conf_file[before] = line.strip()
        print (self.conf_file)

        pass
    def update_config(self):
        pass
    def add_config(self):
        pass
    def delete_config(self):
        pass
    def search_str_in_file(self,search_str):
        with open(self.conf_file,'r') as f:
            for line in f.readline():
                if search_str in line:
                    return True
        return False
    def start(self):
        while not self.is_exit:
            print ('0:查看文件')
            print ('1:增加条目')
            print ('2:删除条目')
            print ('3:退出')
            num = int(input('input you choose:'))
            if num == 3:
                self.is_exit =True
                break
            if num == 0:
                self.print_config()
                continue
            if num == 1:
                self.add_config()
                continue
            if num == 2:
                self.delete_config()

a = ConfigFile()
a.load_config()
