import pika
import sys
import os

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))

channel = connection.channel()


routing_key = sys.argv[1]
channel.exchange_declare(exchange='run_cmd',
                         exchange_type='direct')

channel.queue_bind(exchange='run_cmd',
                   queue='rpc_queue',
                   routing_key=routing_key)

def run_cmd(cmd):
    result = os.popen(cmd)
    return result.read()

def on_request(ch, method, props, body):
    cmd = str(body.decode())
    response = run_cmd(cmd)
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