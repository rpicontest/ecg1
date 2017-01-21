#!/bin/bash

echo ""
echo "Digi Temp"
echo ""
echo "DS18B20		-> Raspberry Pi 3"
echo "-------------------------------------"
echo "Pin G		-> Pin 6 (GND)"
echo "Pin R (3.3V)	-> Pin 1 (3.3V)"
echo "Pin Y (SIG)	-> Pin 7 (GPIO 04)"
echo ""

sudo modprobe w1-gpio
sudo modprobe w1-therm

TEMPFILE=`ls /sys/bus/w1/devices/28*/w1_slave`
cat $TEMPFILE
echo ""
TEMP=`cat $TEMPFILE | grep 't=' | cut -d' ' -f10 | cut -d'=' -f2`
TEMP1=`python -c "print($TEMP. / 1000.)"`
TEMP2=$(expr $TEMP / 1000)

echo "TEMP=$TEMP C	(nicht konvertiert)"
echo "TEMP1=$TEMP1 C	(Python, korrekt)"
echo "TEMP2=$TEMP2 C	(Bash, gerundet, ungenügend)"
