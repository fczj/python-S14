#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-30 下午3:34
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 广播-生产者.py
# @Software: PyCharm




import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()