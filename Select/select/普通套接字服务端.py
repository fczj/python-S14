#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-29 上午9:58
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 普通套接字服务端.py
# @Software: PyCharm


import socket

SOCKET_FAMILY = socket.AF_INET
SOCKET_TYPE = socket.SOCK_STREAM

sockServer = socket.socket(SOCKET_FAMILY, SOCKET_TYPE)
sockServer.bind(('0.0.0.0', 8888))
sockServer.listen(5)

while True:
    cliobj, addr = sockServer.accept()
    while True:
        recvdata = cliobj.recv(1024)
        if recvdata:
            print(recvdata.decode())
        else:
            cliobj.close()
            break