#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-23 上午9:41
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : ftp_server.py
# @Software: PyCharm


import os
import sys
pro_path = (os.path.abspath('./'))
sys.path.append(pro_path)
import socket
import utility


sv = socket.socket()
sv.bind(('127.0.0.1',9992))
sv.listen(5)

conn,addr = sv.accept()

while True:
    cmd = conn.recv(1024)
    op,file,*_= cmd.decode().split(' ')
    print (op,file)
    file_size = os.stat(file).st_size
    file_md5 = utility.md5(file)
    print (file_size,file_md5)
    file_info = str(file_size)+' '+str(file_md5)
    conn.send(file_info.encode())
    client_ack = conn.recv(1024)
    print (client_ack.decode())

    with open(file,'rb') as f:
        for block in iter(lambda :f.read(1024),b''):
            conn.send(block)



