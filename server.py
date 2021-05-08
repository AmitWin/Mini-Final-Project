import socket
from _thread import *
from board import Board
import pickle
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "localhost"
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen()
print("[START] Waiting for a connection")

connections = 0

games = {0: Board()}

def threaded_client(conn, game):
    global pos, games, currentId, connections

    name = None
    bo = games[game]

    if connections % 2 == 0:
        currentId = "w"
    else:
        currentId = "b"

    bo.start_user = currentId

    # Pickle the object and send it to the server
    data_string = pickle.dumps(bo)

    if currentId == "b":
        bo.ready = True
        bo.startTime = time.time()

    conn.send(data_string)
    connections += 1

    while True:
        if game not in games:
            break

        try:
            d = conn.recv(1024 * 32)
            data = d.decode("utf-8")
            if not d:
                break
            else:
                if data.count("select") > 0:
                    all = data.split(" ")
                    col = int(all[1])
                    row = int(all[2])
                    bo.select(col, row)

                if data == "winner b":
                    bo.winner = "b"
                    print("Player b won the game", game)
                if data == "winner w":
                    bo.winner = "w"
                    print("Player w won the game", game)

                if data == "update moves":
                    bo.update_moves()

                if data.count("name") == 1:
                    name = data.split(" ")[1]
                    if currentId == "b":
                        bo.p2Name = name
                    elif currentId == "w":
                        bo.p1Name = name

                print("Received board from", currentId, "in game", game)

                if bo.ready:
                    if bo.turn == "w":
                        bo.time1 = 300 - (time.time() - bo.startTime)
                    else:
                        bo.time2 = 300 - (time.time() - bo.startTime)

                sendData = pickle.dumps(bo)
                print("Sending board to player", currentId, "in game", game)

            conn.sendall(sendData)

        except Exception as e:
            print(e)

    connections -= 1
    try:
        del games[game]
        print("[GAME] Game", game, "ended")
    except:
        pass
    print("[DISCONNECT] Player", name, "left game", game)
    conn.close()

while True:
    if connections < 6:
        conn, addr = s.accept()
        g = -1
        print("[CONNECT] New connection")

        for game in games.keys():
            if not games[game].ready:
                g = game

        if g == -1:
            try:
                g = list(games.keys())[-1] + 1
                games[g] = Board()
            except:
                g = 0
                games[g] = Board()

        print("[DATA] Number of Connections:", connections + 1)
        print("[DATA] Number of Games:", len(games))

        start_new_thread(threaded_client, (conn, g))
