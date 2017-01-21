#!/bin/bash

rrdtool create 05_dashbutton.rrd \
--step '300' \
'DS:dashbutton:GAUGE:600:0:1' \
'RRA:AVERAGE:0.5:288:1'
