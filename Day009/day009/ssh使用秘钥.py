#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-25 上午11:48
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : ssh使用秘钥.py
# @Software: PyCharm

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('/home/xiongzhibiao/.ssh/id_rsa')

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.1.166', port=22, username='xiongzhibiao', pkey=private_key)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('df')
result = stdout.read()
print(result.decode())
stdin, stdout2, stderr = ssh.exec_command('ifconfig')
# 获取命令结果
result2 = stdout2.read()
print(result2.decode())

# 关闭连接
ssh.close()



