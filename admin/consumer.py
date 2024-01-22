import pika, json, django, os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product


params = pika.URLParameters('amqps://mqakmgxd:dwA0XzPUP_E8tFu1QLrxnJMeX7dWfsQA@moose.rmq.cloudamqp.com/mqakmgxd')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    print('Trying my best to increase the likes count!')
    data = json.loads(body)
    print('data: ', data)

    product = Product.objects.get(id=data)
    print(product)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')

channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming')

channel.start_consuming()

channel.close()