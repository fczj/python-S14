#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-31 上午9:26
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 路由-rpc-server.py
# @Software: PyCharm

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = ['info','error']

for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print (' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print (" [x] %r:%r" % (method.routing_key, body,))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
