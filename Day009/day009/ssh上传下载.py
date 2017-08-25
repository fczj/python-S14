#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-25 上午11:37
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : ssh上传下载.py
# @Software: PyCharm


import paramiko
transport = paramiko.Transport(('192.168.1.166', 22))
transport.connect(username='xiongzhibiao', password='cdlanjing')
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put('./ROOT.war', '/tmp/ROOT.war')
#sftp.get('/home/xiongzhibiao/ROOT.war', './ROOT.war')

transport.close()