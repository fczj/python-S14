#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-22 下午3:04
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 客户端.py
# @Software: PyCharm


import  socket
import os


cl = socket.socket()
cl.connect(('127.0.0.1',9996))

while True:
    cmd = input('>>').strip()               #发送执行的命令
    cl.send(cmd.encode())                   #发送编码
    size = cl.recv(1024).decode()           #接受返回的大小
    print ("大小:",size,type(size))
    f = open('/tmp/revcive','wb')
    recive_size = 0
    while recive_size < int(size):
        recive_data = cl.recv(1024)
        recive_size += len(recive_data)
        f.write(recive_data)
    f.close()



