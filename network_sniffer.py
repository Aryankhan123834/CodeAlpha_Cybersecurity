import scapy.all as scapy
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto
        proto_name = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}.get(proto, str(proto))
        print(f"[+] Packet: {src_ip} -> {dst_ip} | Protocol: {proto_name}")
        if TCP in packet:
            print(f"    TCP Payload: {bytes(packet[TCP].payload)[:32]}")
        elif UDP in packet:
            print(f"    UDP Payload: {bytes(packet[UDP].payload)[:32]}")
        elif ICMP in packet:
            print(f"    ICMP Payload: {bytes(packet[ICMP].payload)[:32]}")
        else:
            print(f"    Other Payload: {bytes(ip_layer.payload)[:32]}")
        print("-")

def main():
    print("Starting basic network sniffer... (Press Ctrl+C to stop)")
    scapy.sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
