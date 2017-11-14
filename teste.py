#coding: utf-8

import pika


conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

chan = conn.channel()

chan.queue_declare(queue='errors')

chan.basic_publish(
    exchange='',
    routing_key='errors',
    body='Error on client'
)

print('Message was sent')

chan.close()
