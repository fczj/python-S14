#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-21 下午9:24
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : client.py
# @Software: PyCharm

import socket



client = socket.socket()        #初始化实例
address = ('127.0.0.1',9999)    #地址
client.connect(address)         #连接
client.send('下载电影'.encode('utf-8'))     #发送，只支持二进制的发送
client.close()
