import socket
import pickle
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
            self.client.send(str.encode(pseudo))
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            receive = self.client.recv(2048*4)
            # return pickle.loads(receive)
            # print("receive packet len: ", len(receive))
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
