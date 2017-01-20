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
# Python Installer
sudo apt-get -y install python-pip python3-pip
# Dash Button
sudo apt-get -y install scapy tcpdump

# Abschluss
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
