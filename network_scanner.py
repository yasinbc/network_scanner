import scapy.all as scapy

def scan(ip):
    #pregunta a la maquina quien tiene este IP
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether()
    #lista las MACs asociadas
    scapy.ls(scapy.Ether())

#    scapy.arping(ip)

#comprobar antes con sudo route -n
#ejecutar con SUDO
scan("192.168.100.1/24")