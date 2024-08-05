# ids.py
from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP
import logging
from collections import defaultdict
import time

logging.basicConfig(filename='alerts.log', level=logging.INFO)

# Initialize comprehensive traffic statistics
traffic_stats = {
    'total_packets': 0,
    'udp_traffic': defaultdict(int),
    'tcp_traffic': defaultdict(int),
    'other_traffic': defaultdict(int),
    'alerts': [],
    'packet_times': []
}

def packet_callback(packet):
    traffic_stats['total_packets'] += 1
    traffic_stats['packet_times'].append(time.time())
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        # Handle UDP packets
        if packet.haslayer(UDP):
            udp_layer = packet.getlayer(UDP)
            traffic_stats['udp_traffic'][ip_layer.src] += 1
            check_udp_flood(ip_layer, udp_layer)
        # Handle TCP packets
        elif packet.haslayer(TCP):
            tcp_layer = packet.getlayer(TCP)
            traffic_stats['tcp_traffic'][ip_layer.src] += 1
        # Count other types of traffic
        else:
            traffic_stats['other_traffic'][ip_layer.src] += 1

def check_udp_flood(ip_layer, udp_layer):
    key = (ip_layer.src, udp_layer.dport)
    if traffic_stats['udp_traffic'][ip_layer.src] > 10:
        alert = f"UDP Flood Alert: {ip_layer.src} -> {ip_layer.dst} (Port: {udp_layer.dport})"
        print(alert)
        logging.info(alert)
        traffic_stats['alerts'].append(alert)

def start_sniffing(interface):
    sniff(iface=interface, prn=packet_callback, store=0)

def update_settings(new_settings):
    pass  # Implement settings update logic
