import psutil
import pyshark


interfaces = psutil.net_if_addrs()
address = interfaces['Wi-Fi']
for addr in address:
        ip_address = addr.address
        print(ip_address)
        
capture = pyshark.LiveCapture(interface='Wi-Fi')
while True:
        capture.sniff(timeout=0.1)
        for packet in capture:
                
                print(dir(packet))
                
                # print("Source IP: ", packet.ip.src)
                # print("Destination IP: ", packet.ip.dst)
                # # print("Source Port: ", packet.tcp.srcport)
                # # print("Destination Port: ", packet.tcp.dstport)
                # print("Protocol: ", packet.eth)
                # # print("Protocol: ", packet.transport_layer)
                # # print("Packet info: ", packet)
                print("______________________________________________________________________________________________")


