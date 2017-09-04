#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-30 下午11:54
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : rpc-cmd-client.py
# @Software: PyCharm
import pika
import uuid

response_dict = {}

class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))

        self.channel = self.connection.channel()






def check_task(id):
    print (id)
    if id in response_dict:
        print ('获取命令')
        ret =  response_dict[id]
        del response_dict[id]
        return ret
    else:
        return b'task is running'

def list():
    for task_id in response_dict.keys():
        print (task_id)

while True:
    cmd = input('>>')
    if 'check' in cmd:
        id = cmd.split(' ')[1]
        ret = check_task(id)
        print (ret.decode())
        continue
    if 'list' in cmd:
        list()
        continue
    fibonacci_rpc = FibonacciRpcClient()
    fibonacci_rpc.call(cmd)
    print ("task-id:{}".format(fibonacci_rpc.corr_id))
