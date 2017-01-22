#!/usr/bin/env python

import ADC0832
import time
import math
import ssl
import time
from datetime import datetime

varWaitTime=30

def init():
	ADC0832.setup()
	print("")
	print("Analog Temperatur")
	print("")
	print("ADC")
	print("ADC		   RPI")
	print("---------------------------------------")
	print("Pin 1		-> Pin 11 (GPIO 17)")
	print("Pin 2		-> (+++Sensor+++)")
	print("Pin 3		-> (+++ ohne +++)")
	print("Pin 4		-> Pin 9  (GND)")
	print("Pin 5 (DI)	-> Pin 13 (GPIO 27)")
	print("Pin 6 (DO)	-> Pin 13 (GPIO 27)")
	print("Pin 7 (CLK)	-> Pin 12 (GPIO 18)")
	print("Pin 8 (VCC)	-> Pin 1  (3.3V)")
	print("")
	print("Sensor (beliebiger analoger Sensor")
	print("Sensor")
	print("---------------------------------------")
	print("Pin -		-> Pin 9  (GND)")
	print("Pin +		-> Pin 1  (3.3V)")
	print("Pin S		-> (+++Pin 2 ADC+++)")
	print("")

def loop():
	while True:
		gas = ADC0832.getResult()
		gas = float("{0:.2f}".format(gas))

		t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print '%s Gas Level = %.2f SnO2 (Wartezeit: %ss)' % (t, gas, varWaitTime)

#		try:
		context = ssl._create_unverified_context()

		url = open('/home/pi/circonus/ecg1_sensors_url.txt', 'r').read()
#			print 'URL=%s' % url

		import json
		import urllib2

		data = {
      	 		'ECG1.SnO2_gas': gas
		}

		req = urllib2.Request(url)
		req.add_header('Content-Type', 'application/json')

		response = urllib2.urlopen(req, json.dumps(data), context=context)
#		except:
#			pass

		time.sleep(varWaitTime)

if __name__ == '__main__':
	init()

	try:
		loop()
	except KeyboardInterrupt: 
		ADC0832.destroy()
		print 'The end !'
