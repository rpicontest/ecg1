#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import requests
import sys

BtnPin = 22
PROBE_TIMER = 60 # Anzahl Sekunden, die ein Standwaert gesendet werden soll

# #######################################################


ARG_DISPLAY=0
for arg in sys.argv:
        if arg == "-display":
                ARG_DISPLAY=1


if ARG_DISPLAY == 1:
	print "DEMO: Pressure mat"
	print ""
	print "GPIO 25 (Pin 22) -> Kontakt #1 Matte"
	print "GRND    (Pin 20) -> Kontakt #2 Matte"
	print ""
	print "Ausgabe:"



def setup():
        GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
        GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
        GPIO.add_event_detect(BtnPin, GPIO.BOTH, callback=detect, bouncetime=200)

def Print(x):
        if x == 0:
		if ARG_DISPLAY == 1:
 	               print '    *************************'
	               print '    *   Matte ausgeloest!   *'
	               print '    *************************'
                Status(1)


def Status(sensordata):
	if ARG_DISPLAY == 1:
		print "Status=",sensordata

def detect(chn):
        Print(GPIO.input(BtnPin))

def destroy():
        GPIO.cleanup()                     # Release resource

setup()
try:
  while True:
    True
    time.sleep(PROBE_TIMER)
    Status(0)

except KeyboardInterrupt:
  destroy()

