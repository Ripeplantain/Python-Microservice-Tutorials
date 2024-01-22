import pika, json


params = pika.URLParameters('amqps://mqakmgxd:dwA0XzPUP_E8tFu1QLrxnJMeX7dWfsQA@moose.rmq.cloudamqp.com/mqakmgxd')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)