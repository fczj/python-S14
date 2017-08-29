#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-29 上午10:32
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : select并发.py
# @Software: PyCharm

from select import select
import queue
import socket

server_ip = ('127.0.0.1',9988)
server = socket.socket()
server.bind(server_ip)
server.listen(5)


inputlst = []
outputlst = []
msg_que = {}
if __name__ == "__main__":
    inputlst.append(server)
    stdin,stdout,err = select(inputlst,outputlst,inputlst)

    for obj in stdin:
        if obj == server:
            print ('有新的链接进来')


