#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-22 下午3:04
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 服务器端_ssh.py
# @Software: PyCharm

import socket
import os
import time

sv = socket.socket()
sv.bind(('127.0.0.1',9997))
sv.listen(5)

conn,addr = sv.accept()

while True:
    cmd = conn.recv(1024)
    send = os.popen(cmd.decode()).read()
    print ('返回数据:')
    print (send)
    print (str(len(send)))
    conn.send(str(len(send)).encode())
    #time.sleep(1)
    #开发过程中必须注意粘包的问题,两次都是send,第一次第二次的数据会一起发送,导致接收方解析错误
    #这儿发的次数,如果不睡眠,那么发送的次数和后面的数据会一起发送
    #使用sleep
    client_ack= conn.recv(1024)
    print (client_ack.decode())
    conn.send(send.encode())
