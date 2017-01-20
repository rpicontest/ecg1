#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import requests

BtnPin = 22
PROBE_TIMER = 60 # Anzahl Sekunden, die ein Standwaert gesendet werden soll

# #######################################################

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
                print '    *************************'
                print '    *   Matte ausgeloest!   *'
                print '    *************************'
#                PowerBI(1)
                Status(1)

def PowerBI(sensordata):
        import urllib, urllib2
        from datetime import datetime
        try:
                now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S%Z")
                #data = '[{"pressuremat" :1, "timestamp" : ',now,'}]'
                data = '[{{ "timestamp": "{0}", "pressuremat": "{1}" }}]'.format(now, sensordata)
                POWERAPI_URL = "https://api.powerbi.com/beta/75268b71-c41e-4e48-8eb7-fae92fe84d8f/datasets/a7ef0c85-4231-4041-a7e1-53218f8c2337/rows$key=Jk95ydrfFhYJkB4kn%2FG3fgAq87bplGs3R2zrzYWJpyu6BPj03v%2B2VimzA1N02cQIvdwoRMXfBcytEh9NRs3fTA%3D%3D"

                print "URL : ",POWERAPI_URL
                print "DATA: ",data
                req = urllib2.Request(POWERAPI_URL, data)
                response = urllib2.urlopen(req)
                print("POST request to Power BI with data:{0}".format(data))
                print("Response: HTTP {0} {1}\n".format(response.getcode(), response.read()))
                #requests.post(POWERAPI_URL, data=data)
                time.sleep(1)
        except urllib2.HTTPError as e:
                print("HTTP Error: {0} - {1}".format(e.code, e.reason))
        except urllib2.URLError as e:
                print("URL Error: {0}".format(e.reason))
        except Exception as e:
                print("General Exception: {0}".format(e))

def Status(sensordata):
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
#    PowerBI(0)
    Status(0)

except KeyboardInterrupt:
  destroy()

