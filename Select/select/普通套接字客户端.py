#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-29 上午9:58
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 普通套接字客户端.py
# @Software: PyCharm

import socket


# def send(i):
socCli = socket.socket()
socCli.connect(('127.0.0.1', 1239))
socCli.send(str(1).encode())

# for i in range(50):
#     send(i)


