import paho.mqtt.client as mqtt

MQTT_SERVER = "127.0.0.1" # other raspi IP adress
MQTT_PATH   = "channel_1" # topic to subscriber

temp = 0.0
cycle = 1

def on_connect (client, userdata, flags, rc):
    client.subscribe(MQTT_PATH)
    print("Conenected to TOPIC")

def on_message(client, userdata, msg):
    #print("Topic " + msg.topic + " message: " + str (msg.payload)) # for visualization
    temp = float(msg.payload)
    

client = mqtt.Client()
client.on_connect = on_connect()
client.on_message = on_message()

client.connect(MQTT_SERVER, 1883, 60)
client.loop_start()                    # update loop while parallely running the script

while True:
    
    print("temperature:", temp)

