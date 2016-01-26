#!/bin/sh
nohup python $RabbitMQdir/listener.py > $RabbitMQdir/log/listener.log 2>&1 &
