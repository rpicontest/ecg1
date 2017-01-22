#!/bin/bash
sudo chmod 777 /etc/iptables/rules.v4
sudo chmod 777 /etc/iptables/rules.v6
sudo iptables-save > /etc/iptables/rules.v4
sudo ip6tables-save > /etc/iptables/rules.v6
