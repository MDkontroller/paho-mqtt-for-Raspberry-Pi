import paho.mqtt.client as mqtt
import paho.mqtt.publish as pb
from time import sleep

MQTT_SERVER = "127.0.0.1" #169.254.71.208" local network()
MQTT_PATH   = "channel_1" # topic to be publish /subscribed

temp = 0.0
cycle = 1
t = 0.0

def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_PATH)
    print("Connected.  result:" +str(rc))

def on_message(client,userdata,msg):
	print("topic:"+ msg.topic + "  distance: " +str(msg.payload))
	#temp = float(msg.payload)
	temp = float(msg.payload)
	


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#client.connect(MQTT_SERVER, 1883, 60)
client.connect(MQTT_SERVER)
client.loop_start()

while True:
    
    sleep(0.02)
    temp += 1   
    pb.single(MQTT_PATH, temp, hostname = MQTT_SERVER)
