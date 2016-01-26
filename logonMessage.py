#!/usr/bin/python
import pika
import time
import datetime
import sys
import os

# Use plain credentials for authentication
mq_creds  = pika.PlainCredentials(
    username = "webmessage",
    password = "guest")

# Use localhost
mq_params = pika.ConnectionParameters(
    host         = "sjholt02.servebeer.com",
    credentials  = mq_creds,
    virtual_host = "/")

mq_exchange    = "amq.topic"
mq_routing_key = "PiCloud"

# This a connection object
mq_conn = pika.BlockingConnection(mq_params)

# This is one channel inside the connection
mq_chan = mq_conn.channel()

text = os.environ['USER'] 
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
message_text = st + " INFO : Logon By: " + text
mq_chan.basic_publish(
      	exchange    = mq_exchange,
      	routing_key = mq_routing_key,
      	body        = message_text)

