
#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import paho.mqtt.publish as pb
from time import sleep

MQTT_SERVER = "127.0.1.1"

temp = 0.0
humidity = 0.0

client = mqtt.Client()      
client.connect(MQTT_SERVER)             
client.loop_start()

while True:
    
    temp +=1
    humidity +=10
    sleep(0.2)
    msgs = [{'topic': "temperature",'payload': temp},{'topic':"humidity",'payload': humidity}]
    pb.multiple(msgs,hostname=MQTT_SERVER)