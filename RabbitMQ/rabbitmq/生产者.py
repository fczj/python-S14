#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-30 上午9:25
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 生产者.py
# @Software: PyCharm


import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()