import scapy.all as scapy

def scan(ip):
    #pregunta a la maquina quien tiene este IP
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    #pregunta a cada subnet quien tiene nuestra IP
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]

    for element in answered_list:
        print("IP>  ["+element[1].psrc+"]")
        print("MAC> ["+element[1].hwsrc+"]")
        print("---------------------------------------------------")

#    scapy.arping(ip)

#comprobar antes con "sudo route -n"
#ejecutar con SUDO
scan("IP_ROUTER/24")