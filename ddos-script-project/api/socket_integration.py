import socket

class SocketIntegration:
    def __init__(self, target_ip, target_port):
        self.target_ip = target_ip
        self.target_port = target_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_ddos_packet(self, packet):
        self.sock.sendto(packet, (self.target_ip, self.target_port))

    def close_connection(self):
        self.sock.close()

    def receive_response(self):
        response, _ = self.sock.recvfrom(1024)
        return response

    def establish_connection(self):
        self.sock.connect((self.target_ip, self.target_port))

    def send_encrypted_packet(self, encrypted_packet):
        self.sock.send(encrypted_packet)

    def receive_encrypted_response(self):
        encrypted_response = self.sock.recv(1024)
        return encrypted_response

    def set_timeout(self, timeout):
        self.sock.settimeout(timeout)