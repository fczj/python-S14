#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-21 下午9:29
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : server.py
# @Software: PyCharm

import  socket


server = socket.socket()
address = ('127.0.0.1',9999)
server.bind(address)
server.listen(5)

conn,addr = server.accept()         #阻塞等待数据
#conn       客户端连接过来时，服务器端为其生成的实例
#addr       客户端信息
print(conn,addr)


rc = conn.recv(1024)
server.close()
print (rc.decode('utf-8'))
