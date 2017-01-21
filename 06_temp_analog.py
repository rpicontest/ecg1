#!/usr/bin/env python
import ADC0832
import time
import math

def init():
	ADC0832.setup()
	print("")
	print("Analoge Temperatur")
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
		analogVal = ADC0832.getResult()
#		print 'temp analog= %d C' % analogVal
		Vr = 5 * float(analogVal) / 255
		Rt = 10000 * Vr / (5 - Vr)
		temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
		temp = temp - 273.15
		print 'Temperatur = %d C' % temp
		time.sleep(0.5)

if __name__ == '__main__':
	init()
	try:
		loop()
	except KeyboardInterrupt: 
		ADC0832.destroy()
		print 'The end !'
