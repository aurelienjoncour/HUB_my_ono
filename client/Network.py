import socket
import json
import zlib

class Network:
    def __init__(self, ip_address, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip_address = ip_address
        self.port = port
        self.addr = (self.ip_address, self.port)

    def connect(self, pseudo):
        try:
            self.client.connect(self.addr)
        except:
            print("Could not connect to: ", self.ip_address)
            return None
        try:
            self.client.send(str.encode(pseudo))
            return self.client.recv(2048).decode()
        except:
            print("Unable to send init packet to server: ", self.ip_address)
            return None

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            receive = self.client.recv(2048*4)
            try:
                decompress_data = zlib.decompress(receive)
                load = json.loads(decompress_data)
            except json.decoder.JSONDecodeError:
                print("String could not be converted to JSON: receive")
                print(receive)
                load = None
            return load
        except socket.error as e:
            print(e)
