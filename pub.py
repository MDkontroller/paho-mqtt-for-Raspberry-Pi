import paho.mqtt.client as mqtt
import paho.mqtt.publish as pb
from time import sleep

MQTT_SERVER = "127.0.0.1" #169.254.71.208" local network()
MQTT_PATH   = "channel_1" # topic to be publish /subscribed

Temp = 0.0
cycle = 1

def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_PATH)
    print("Connected.  result:" +str(rc))

def on_message(client,userdata,msg):
	#print("topic:"+ msg.topic + "  distance: " +str(msg.payload))
	distance = float(msg.payload)
	print("Distance = ",distance)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)
client.loop_start()

while True:
   
    pb.single(MQTT_PATH, temp, hostname = MQTT_SERVER)