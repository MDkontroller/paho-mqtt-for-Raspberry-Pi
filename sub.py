#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from time import sleep

MQTT_SERVER = "169.254.x.x" # other raspi IP adress
MQTT_PATH   = "channel_1" # topic to subscriber

temp = 0.0
cycle = 0

def on_connect (client, userdata, flags, rc):
    client.subscribe(MQTT_PATH)
    #print("Conenected to TOPIC")

def on_message(client, userdata, msg):
    #print("Topic " + msg.topic + " message: " + str (msg.payload)) # for visualization
    global temp
    #global cycle 
    temp = float(msg.payload)
   
    
def connection():
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_SERVER, 1883, 60)
    client.loop_start()
    client.disconnect()

while True:
    
    sleep(0.5)
    connection()
    print(temp)
