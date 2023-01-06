import scapy.all as scapy

def scan(ip):
    #pregunta a la maquina quien tiene este IP
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request

    #pregunta a cada subnet quien tiene nuestra IP
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    print(answered.summary())


#    scapy.arping(ip)

#comprobar antes con sudo route -n
#ejecutar con SUDO
scan("192.168.100.1/24")