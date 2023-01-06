import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

#ejecutar con sudo
scan("IP_LOCAL/24")