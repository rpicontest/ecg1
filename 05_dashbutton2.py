import logging # for the following line

logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # suppress IPV6 warning on startup

from scapy.all import * # for sniffing for the ARP packets
import requests # for posting to the IFTTT Maker Channel
 
# it takes a minute for the scapy sniffing to initialize, so I print this to know when it's actually ready to go
print('Init Amazon Dash Button sniffer... done.')
 
def button1_pressed(mac) :
  print('')
  print('######################################################')
  print('### Amazon Dash Button pressed (' + mac + ') ###') 
  print('######################################################')

def arp_display(pkt):
  mac_actions = { 'ac:63:be:c6:28:af' : button1_pressed }
  mac_list = list(mac_actions.keys())

#  print('------------------')
#  print('method init...')
#  print('hw.src=' + pkt[ARP].hwsrc)
#  print('hw.psrc=' + pkt[ARP].psrc)
  if pkt[ARP].op == 1: #who-has (request)
      if pkt[ARP].hwsrc in mac_list : # this is the first button MAC address
        mac_actions[pkt[ARP].hwsrc](pkt[ARP].hwsrc)
#      else:
#        print("ARP Probe from unknown device: " + pkt[ARP].hwsrc)
 
print(sniff(prn=arp_display, filter="arp", store=0))
