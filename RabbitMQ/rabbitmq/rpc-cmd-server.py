#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-30 下午11:53
# @Author  : xiongzhibiao
# @Email   : 158349411@qqcom
# @File    : rpc-cmd-server.py
# @Software: PyCharm

import pika
import os

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='run_cmd',
                         exchange_type='direct')

def run_cmd(cmd):
    result = os.popen(cmd)
    return result.read()

def on_request(ch, method, props, body):
    response = run_cmd(body.decode())
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                     props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print (" [x] Awaiting RPC requests")
channel.start_consuming()