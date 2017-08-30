#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-30 上午9:53
# @Author  : xiongzhibiao
# @Email   : 158349411@qq.com
# @File    : 消费者.py
# @Software: PyCharm


import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch,method,properties,body):
    print('recived message {}'.format(body))

channel.basic_consume(callback,
                       queue='hello',
                       no_ack=True
)

print('waiting for message')
channel.start_consuming()

