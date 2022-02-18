from _thread import *
import pickle
from game.Game import Game
from random import randrange
import socket

class Server:
    def __init__(self, address, port):
        self.port = port
        self.ip_address = address
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.ip_address, self.port))
        self.nb_connection = 0
        self.games = {}

    def listen(self):
        self.server.listen(2)
        print("Listening on port %d" % self.port)

    def handle_client(self, conn, player, gameId):

        while True:
            try:
                data = conn.recv(4096).decode()

                if gameId in self.games:
                    game = self.games[gameId]

                    print("data receive: ", data)
                    if not data:
                        break
                    else: 
                        if data == "play":
                            print("play")
                        dump = pickle.dumps(game)
                        print("Size:", len(dump))
                        conn.sendall(dump)

            except:
                break
        print("Lost connection")
        self.nb_connection -= 1
        conn.close()

    def accept_client(self):
        conn, addr = self.server.accept()
        print("Connected to:", addr)
        player = conn.recv(2048).decode()
        playerId = randrange(9999)
        conn.sendall(str.encode(str(playerId)))

        self.nb_connection += 1
        gameId = (self.nb_connection - 1)//2
        if self.nb_connection % 2 == 1:
            self.games[gameId] = Game(gameId)
            self.games[gameId].addPlayer(player, playerId)
            print("Create a new game: id ", gameId)
        else:
            self.games[gameId].addPlayer(player, playerId)
            self.games[gameId].start()

        
        print("Active connnection:", self.nb_connection)

        start_new_thread(self.handle_client, (conn, player, gameId))
