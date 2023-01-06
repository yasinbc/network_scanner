import scapy.all as scapy

def scan(ip):
    #pregunta a la maquina quien tiene este IP
    arp_request = scapy.ARP(pdst = ip)
    arp_request.show() #Parametros ARP
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    broadcast.show() #Parametros MAC
    arp_request_broadcast = broadcast/arp_request


#    scapy.arping(ip)

#comprobar antes con sudo route -n
#ejecutar con SUDO
scan("192.168.100.1/24")