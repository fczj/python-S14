#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-23 上午9:41
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : ftp_client.py
# @Software: PyCharm

import os
import sys
pro_path = (os.path.abspath('./'))
sys.path.append(pro_path)
import socket
import utility
import  socket
import os

cl = socket.socket()
cl.connect(('127.0.0.1',9992))

while True:
    cmd = input('>>').strip()
    cl.send(cmd.encode())
    print ("下载文件命令:",cmd)

    file_size,file_md5 = cl.recv(1024).decode().split(' ')
    file_size = int(file_size)
    print (file_size,file_md5)
    cl.send('client:recive file info'.encode())

    recive_size = 0
    with open('/tmp/test','wb') as f:
        while recive_size < file_size:
            recive_data = cl.recv(1024)
            f.write(recive_data)
            recive_size += len(recive_data)
            print('{}==>{}'.format(recive_size,file_size))

    recive_file_md5 =utility.md5('/tmp/test')
    if file_md5 == recive_file_md5:
        print ('file is recive done and is ok;')






'''
1.客户端发送获取文件的命令--get开头
2.服务端接收命令--解析
3.判断文件存在,并读取文件大小
4.传送文件大小,md5信息,文件名
5.客户端回复ack
6.服务端收到ack后开始发送数据
7.传送完成后验证
'''

