#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-26 下午10:08
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : batchrun.py
# @Software: PyCharm


import paramiko
import threading

class RunCmd():
    def __init__(self,user,host,password,port=22):
        self.user = user
        self.port = port
        self.host = host
        self.password = password

    def run_cmd(self,cmd):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=self.host, port=self.port,
                    username=self.user,password=self.password)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        res,err = stdout.read(),stderr.read()
        result = res if res else err
        ssh.close()
        return result.decode()


class MulitiRun():
    def __init__(self):
        pass


a = RunCmd(user='lanjing',host='127.0.0.1',password='cdlanjing')
b = a.run_cmd('pwd')
print (b)
