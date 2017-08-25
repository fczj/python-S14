#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-25 上午10:50
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : ssh客户端执行命令.py
# @Software: PyCharm

import paramiko
# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.1.166', port=22, username='xiongzhibiao', password='cdlanjing')
while True:
    cmd = input('>>:')
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(cmd)
    # 获取命令结果
    res,err = stdout.read(),stderr.read()
    result = res if res else err
    print(result.decode())
    # 关闭连接
ssh.close()
