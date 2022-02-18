from server.Server import Server

ip_address = ""
port = 8080

gameServer = Server(ip_address, port)

gameServer.listen()
while True:
    gameServer.accept_client()