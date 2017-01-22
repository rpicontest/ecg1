#!/bin/bash

DASHBUTTON=AC:63:BE:C6:28:AF
#DASHBUTTON=CC:20:E8.64.0A:7E
ALLOWED1=CC:20:E8:64:0A:7F

sudo iptables --flush

sudo iptables -t nat -I PREROUTING -j DNAT --destination 8.8.8.8 --to 10.11.12.1
sudo iptables -t nat -I PREROUTING -j DNAT --destination 8.8.4.4 --to 10.11.12.1

sudo chmod 777 /etc/iptables/rules.v4
sudo iptables-save > /etc/iptables/rules.v4
