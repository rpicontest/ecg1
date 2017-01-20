#!/bin/bash

# #####################################################
# 1. Initialisierung
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y autoremove
# Tools
sudo apt-get -y install mc
sudo apt-get -y install htop
sudo apt-get -y install git-core
# Bluetooth
sudo apt-get -y install bluetooth bluez
# Python
sudo apt-get -y install python-gobject python-gobject-2 python-bluez python-dev python-rpi.gpio python-requests

sudo apt-get -y install python-pip
sudo apt-get -y install python3-pip
sudo pip install beebotte
sudo apt-get -y autoremove

# #####################################################
# 2. WiringPi installieren (für SensorPack)
cd ~
mkdir git
cd git
# Sensor-Beispiele installieren
git clone https://github.com/sunfounder/SunFounder_SensorKit_for_RPi2.git
# WiringPi installieren
git clone git://git.drogon.net/wiringPi
cd wiringPi
git pull origin
./build
