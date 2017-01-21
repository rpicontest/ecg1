#!/bin/bash
THISHOST=`hostname`

BASEDIR="/home/pi/$THISHOST"
DATABASE="05_dashbutton.rrd"

echo "Basisverzeichnis: $BASEDIR"
cd $BASEDIR
echo "Datenbank: $DATABASE"

RRD_STEP=60
RRD_DS=dashbutton
RRD_DST=GAUGE
RRD_HEARTBEAT=120
RRD_MIN=0
RRD_MAX=1

rrdtool create $DATABASE --step $RRD_STEP \
           DS:$RRD_DS:$RRD_DST:$RRD_HEARTBEAT:$RRD_MIN:$RRD_MAX \
	   RRA:AVERAGE:0.5:1:1200
