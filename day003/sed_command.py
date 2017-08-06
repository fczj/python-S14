#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-5 下午7:01
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : sed_command.py
# @Software: PyCharm
import  sys

'''
=================================================================
1.简单实现linux中sed命令
=================================================================
'''

class Sed():
    def __init__(self,*args):
        self.sed_file,self.old_str,self.new_str = args
    def sed(self):
        with open(self.sed_file,'r') as f:
            for line in f:
                print (line.replace(self.old_str,self.new_str).strip())

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print ('{} file str replace_str'.format(sys.argv[0]))
    else:
        sys.argv.pop(0)
        a = Sed(*sys.argv)
        a.sed()
