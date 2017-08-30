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

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        response_dict[self.corr_id] = self.response



def check_task(id):
    print (id)
    if id in response_dict:
        print ('获取命令')
        ret =  response_dict[id]
        del response_dict[id]
        return ret
    else:
        return b'task is running'

while True:
    cmd = input('>>')
    if 'check' in cmd:
        id = cmd.split(' ')[1]
        ret = check_task(id)
        print (ret.decode())
        continue
    fibonacci_rpc = FibonacciRpcClient()
    fibonacci_rpc.call(cmd)
    print ("task-id:{}".format(fibonacci_rpc.corr_id))
