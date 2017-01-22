#!/bin/bash

while true
do
        ONLINE=1


	URL=`cat /home/pi/circonus/rpi_ecg1_url.txt`

        curl -X PUT --insecure "$URL" --data '{
            "RPI.online": "'$ONLINE'"
          }'
        sleep 30
done

