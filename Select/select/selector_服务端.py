#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-29 下午12:54
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : selector_服务端.py
# @Software: PyCharm


import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('localhost', 9998))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)

'''
针对可读事件:
1.客户端发送请求到服务端,服务端接受请求--accept
2.客户端发送数据到服务端,服务端接受请求--read
'''
