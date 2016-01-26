#!/usr/bin/env python
import pika
import time
import datetime
import sys
import os

credentials = pika.credentials.PlainCredentials('webmessage','guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(
                'sjholt02.servebeer.com',
		5672,
		'/',
		credentials))


mq_exchange    = "amq.topic"
mq_routing_key = "PiCloud"

channel = connection.channel()

text = " INFO : Started Listener on Pi Cloud"
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
message_text = st + text
channel.basic_publish(
        exchange    = mq_exchange,
        routing_key = mq_routing_key,
        body        = message_text)

def callback(ch, method, properties, body):
#    print " [x] Received %r" % (body,)
    messageTxt = "%r" % (body,)
    if messageTxt=='get weather':
    	cmd = 'python sendWeather.py' 
    else:
    	cmd = 'python messageReceived.py ' + messageTxt 
#    print cmd
    os.system(cmd)

    jabbercmd = './sendJabberMessage.sh'
    os.system(jabbercmd)

channel.basic_consume(callback,
                      queue='PiCloud',
                      no_ack=True)

channel.start_consuming()

