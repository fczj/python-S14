#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-29 下午2:18
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : select并发客户端.py
# @Software: PyCharm
import socket
import sys
import time

messages = [ b'This is the message. ',
             b'It will be sent ',
             b'in parts.',
             ]
server_address = ('127.0.0.1', 9998)

# Create a TCP/IP socket
socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(21000)]
print(socks)
# Connect the socket to the port where the server is listening
print('connecting to %s port %s' % server_address)
for s in socks:
    s.connect(server_address)

for message in messages:

    # Send messages on both sockets
    for s in socks:
        print('%s: sending "%s"' % (s.getsockname(), message) )
        s.send(message)
    # Read responses on both sockets
    for s in socks:
        data = s.recv(1024)
        print( '%s: received "%s"' % (s.getsockname(), data) )
        if not data:
            print( 'closing socket', s.getsockname() )