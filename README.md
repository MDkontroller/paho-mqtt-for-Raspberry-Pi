# paho-mqtt-for-Raspberry-Pi

An basic example for  for 2 Raspis communication.
Tested on Raspian with Desktop.

Make sure you have install mosquitto broken and paho-mqtt python library

sudo apt-get install -y mosquitto mosquitto-clients

sudo pip install paho-mqtt

-------------------------------------------------------------

pub.py   publisher (raspi 1)creates a topic ""channel_1 where to publish data in strings form.

sub.py   subscriber (raspi 2) gets string and cast it to a float variable, while executing client script.
