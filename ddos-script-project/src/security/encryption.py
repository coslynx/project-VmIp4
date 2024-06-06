import hashlib
import base64

class Encryption:
    def __init__(self):
        self.key = self.generate_key()

    def generate_key(self):
        return hashlib.sha256("super_secret_key".encode()).digest()

    def encrypt_data(self, data):
        cipher = AES.new(self.key, AES.MODE_ECB)
        encrypted_data = cipher.encrypt(pad(data.encode(), AES.block_size))
        return base64.b64encode(encrypted_data).decode()

    def decrypt_data(self, encrypted_data):
        cipher = AES.new(self.key, AES.MODE_ECB)
        decrypted_data = unpad(cipher.decrypt(base64.b64decode(encrypted_data)), AES.block_size)
        return decrypted_data.decode()