from _thread import *
import pickle
from server.Game import Game
from random import randrange
import socket
import json

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

    def handle_client(self, conn, playerId, gameId):

        while True:
            try:
                data = conn.recv(4096).decode()

                if gameId in self.games:
                    game = self.games[gameId]
                    # print("NB card: ", len(game.deck.cards))
                    # print("data receive: ", data)
                    if not data:
                        break
                    else:
                        if data == "skipp2":
                            game.handle_p2_res()
                        elif data == "denounce":
                            game.handle_bluff(True)
                        elif data == "dontdenonce":
                            game.handle_bluff(False)
                        elif data != "get":
                            parsed = data.split(":")
                            if len(parsed) == 2:
                                print(parsed)
                            for idx in range(len(game.players)):
                                if game.players[idx].id == playerId:
                                    if len(parsed) == 2:
                                        game.play_card(game.players[idx].deck[int(parsed[0])], idx, int(parsed[1]))
                                    else:
                                        game.play_card(game.players[idx].deck[int(parsed[0])], idx, None)

                            print("End")
                        gameDict = game.gameToDict()
                        data = json.dumps(gameDict)
                        # dump = pickle.dumps(game)
                        # print("Size:", len(dump))
                        conn.send(data.encode())

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
        gameId = (self.nb_connection - 1)//4
        if self.nb_connection % 4 == 1:
            self.games[gameId] = Game(gameId)
            self.games[gameId].addPlayer(player, playerId)
            print("Create a new game: id ", gameId)
        else:
            self.games[gameId].addPlayer(player, playerId)
            self.games[gameId].start()

        
        print("Active connnection:", self.nb_connection)

        start_new_thread(self.handle_client, (conn, playerId, gameId))
