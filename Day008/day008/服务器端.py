#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-22 下午3:04
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 服务器端.py
# @Software: PyCharm

import socket
import os
import time

sv = socket.socket()
sv.bind(('127.0.0.1',9996))
sv.listen(5)

conn,addr = sv.accept()

while True:
    cmd = conn.recv(1024)
    send = os.popen(cmd.decode()).read()
    print ('返回数据:')
    print (send)
    print (str(len(send)))
    conn.send(str(len(send)).encode())
    time.sleep(1)
    conn.send(send.encode())
