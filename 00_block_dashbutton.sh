#!/bin/bash

DASHBUTTON=AC:63:BE:C6:28:AF
#DASHBUTTON=CC:20:E8.64.0A:7E
ALLOWED1=CC:20:E8:64:0A:7F

sudo iptables --flush

#Rules for blocking your mac addresses
sudo /sbin/iptables -A FORWARD -i eth0 -m mac --mac-source $DASHBUTTON -j DROP
sudo /sbin/iptables -A FORWARD -i wlan0 -m mac --mac-source $DASHBUTTON -j DROP
sudo /sbin/iptables -A FORWARD -i wlan1 -m mac --mac-source $DASHBUTTON -j DROP

# explicit allowing some mac addresses
#sudo /sbin/iptables -A FORWARD -i wlan1 -o eth0 -m mac --mac-source $ALLOWED1 -j ACCEPT

#One final rule to drop all packets which do not match one of the rules above (are not from one of your allowed macs)
sudo /sbin/iptables -A FORWARD -i eth0 -o wlan1 -j DROP
sudo /sbin/iptables -A FORWARD -i wlan1 -o eth0 -j DROP

sudo chmod 777 /etc/iptables/rules.v4
sudo iptables-save > /etc/iptables/rules.v4
