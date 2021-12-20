# paho-mqtt for Raspberry-Pi 

# 1. Quick setup

_A basic example for  for 2 Raspis communication. Tested on Raspian with Desktop.

Make sure you have install mosquitto broken and paho-mqtt python library
and get last update packages. in both Raspberry Pi

```console 

sudo apt-get update
sudo apt upgrade

sudo apt-get install mosquitto
sudo apt-get install -y mosquitto mosquitto-clients
sudo pip3 install paho-mqtt
```
# 2.mosquitto
_Make sure mosquitto service is running on booot

```console
sudo systemctl enable mosquitto
```
and check if running...

```console
sudo systemctl status mosquitto
```
# 3. Python Publischer and Subscriber

pub.py correspods to a publisher (raspi 1), creates a topic ""channel_1 where to publish data in strings form.
sub.py is the subscriber (raspi 2) gets string and cast it to a float variable, while executing client script

# that's all!
for more info check [`official paho-mqtt documentation:`](https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php)
