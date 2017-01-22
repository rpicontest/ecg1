#!/bin/bash

WATCHDOG_FILE=/home/pi/ecg1/watchdog.list
THISSCRIPT=$(readlink -f $0)

echo "Watchdog"
echo "================================="
echo "To install, edit 'sudo nano /etc/crontab' and add '* * * * * root $THISSCRIPT'"
echo ""


while read WATCHDOG_PROCESS; do    
    	echo -n "Prüfe Prozess '$WATCHDOG_PROCESS'..."
	COUNT=`ps -ef | grep "$WATCHDOG_PROCESS" | grep -v "grep" | wc -l`
	if [ $COUNT -eq 0 ]; then
		echo "nicht gefunden!"
		$($WATCHDOG_PROCESS) &
	else
		echo "gefunden. OK"
	fi
done < $WATCHDOG_FILE
