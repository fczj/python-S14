#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-30 下午4:31
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 过滤-生产者.py
# @Software: PyCharm

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'error'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
