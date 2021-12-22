#!/usr/bin/env python3

import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt
from time import sleep

MQTT_SERVER = "127.0.1.1" 
MQTT_TOPIC = [("temperature",0),("humidity",0)]

temperature = 0.0
humidity    = 0.0
counter     = 0

def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_TOPIC)
    print("Connected.  result:" +str(rc))

def on_message(client,userdata,msg):

    global temperature, humidity

    if (msg.topic=="temperature"):
        temperature = float(msg.payload)
    elif(msg.topic == "humidity"):
        humidity =float(msg.payload)

def connection():

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_SERVER)
    client.loop_start()
    client.disconnect()

while True:

    counter+=1
    connection()
    print("counter: " + str(counter) + "  temperature: " + str(temperature)+ "  humidity:  "+ str(humidity))

