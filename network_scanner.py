import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

#comprobar antes con sudo route -n
#ejecutar con SUDO
scan("192.168.100.0/24")