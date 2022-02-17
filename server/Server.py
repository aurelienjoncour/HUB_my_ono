from _thread import *
import socket

class Server:
    def __init__(self, address, port):
        self.port = port
        self.ip_address = address
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.ip_address, self.port))
        self.nb_connection = 0

    def listen(self):
        self.server.listen(2)
        print("Listening on port %d" % self.port)

    def handle_client(self, conn, foo):
        conn.send(str.encode("Hello from server"))

        while True:
            try:
                data = conn.recv(4096).decode()
            except:
                break
        print("Lost connection")
        self.nb_connection -= 1
        conn.close()

    def accept_client(self):
        conn, addr = self.server.accept()
        print("Connected to:", addr)
        
        self.nb_connection += 1
        print("Active connnection:", self.nb_connection)

        start_new_thread(self.handle_client, (conn, 12))
