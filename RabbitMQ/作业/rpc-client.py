import pika
import uuid


class RpcCmd(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))

        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='run_cmd',
                                 exchange_type='direct')

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n,host):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='run_cmd',
                                   routing_key=str(host),
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return self.response



while True:
    host,cmd = input(">>").split(' ')
    rpc = RpcCmd()
    response = rpc.call(cmd,host)
    print (" [.] Got %r" % (response.decode()))