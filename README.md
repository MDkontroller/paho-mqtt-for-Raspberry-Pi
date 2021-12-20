# paho-mqtt for Raspberry-Pi 

# 1.Quick setup

A basic example for  for 2 Raspis communication. Tested on Raspian with Desktop.

Make sure you have install mosquitto broken and paho-mqtt python library
and get last update packages. in both Raspberry Pi

```console 

sudo apt-get update
sudo apt upgrade

sudo apt-get install mosquitto
sudo apt-get install -y mosquitto mosquitto-clients
sudo pip3 install paho-mqtt   # or try next if not instaling..
python3 -m pip install paho-mqtt

```
# 2. Mosquitto
Make sure mosquitto service is running on booot

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

in order to reach communication we need the ip adress our publischer, make sure ip address corresponds to the Network where subscriber is conected.
```console
hostname -I
```
this IP adress tipically 169.254.xxx.xxx for ethernet,we add it to our our pubisher and subscriber files. (see SERVER variable)


# that's all!
for more info check [`official paho-mqtt documentation:`](https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php)
