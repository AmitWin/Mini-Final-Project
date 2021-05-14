import socket
from _thread import *
from lobby import Lobby
import pickle
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "localhost"
port = 5555

server_ip = socket.gethostbyname(server)

connections = 0

games = {}


def main():
    try:
        sock.bind((server, port))

    except socket.error as e:
        print(str(e))

    sock.listen()
    print("[START] Waiting for a connection")

    while True:
        client, addr = sock.accept()
        print("[CONNECT] New Connection")

        lobbyId = int(client.recv(1024).decode())
        if lobbyId == -1:
            lobbyId = id_generator()
            games[lobbyId] = Lobby(client, lobbyId)
            client.send(b"Creating New Lobby " + str(lobbyId).encode())
            print("Created New Lobby")
            games[lobbyId].start()

        elif lobbyId in games.keys():
            if not len(games[lobbyId].clients) == 2:
                games[lobbyId].clients.append(client)
                client.send(b"Joining Into an Existing Lobby")

            else:
                client.send(b"[ERROR] 743: lobby is full")

        else:
            client.send(b"[ERROR] 404: lobby not found")


def id_generator():
    import random
    lobbyId = random.randint(1000, 9999)
    while lobbyId in games.keys():
        lobbyId = random.randint(1000, 9999)

    return lobbyId

main()
