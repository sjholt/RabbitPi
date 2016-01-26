#!/bin/bash
SERVICE='listener'
RabbitMQdir='/home/pi/RabbitMQ'

if ps ax | grep -v grep | grep $SERVICE > /dev/null
then
    python $RabbitMQdir/alert.py " INFO : Listener UP" > $RabbitMQdir/log/listener.log 2>&1
else
    python $RabbitMQdir/alert.py " ALERT: Listener Down - restarting"> $RabbitMQdir/log/listener.log 2>&1
    $RabbitMQdir/startListener.sh
fi
