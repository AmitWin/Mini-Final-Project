import pygame as pg
import threading
import board
import pickle


class Lobby(threading.Thread):
    def __init__(self, client, lobbyId):
        threading.Thread.__init__(self)
        self.lobbyId = lobbyId
        self.clients = [client]

    def run(self):
        while len(self.clients) < 2:
            pass

        for i in range(len(self.clients)):
            self.clients[i].send(b"Starting Game...")
            color = "w" if i == 0 else "b"
            self.clients[i].send(b"You are:" + color.encode())

        self.play()

    def play(self):
        while True:
            board = self.clients[0].recv(1024 * 32)
            self.clients[1].send(board)
            board = self.clients[1].recv(1024 * 32)
            self.clients[0].send(board)

        """
        currentId = 0
        sendBoard = pickle.dumps(self.board)
        for client in self.clients:
            client.send(sendBoard)

        while not self.board.winner:
            color = "white" if currentId == 0 else "black"
            for client in self.clients:
                print("This is " + color + " turn")
                client.send(("This is " + color + " turn").encode())

            sendBoard = pickle.dumps(self.board)
            self.clients[currentId].send(sendBoard)
            print("Sending Board to " + color + "in lobby " + str(self.lobbyId))

            newBoard = self.clients[currentId].recv(1024 * 32)
            self.board = pickle.loads(newBoard)
            print("Received Board From " + color + " in lobby " + str(self.lobbyId))
            currentId = 1 if currentId == 0 else 0

        for client in self.clients:
            client.send((self.board.winner + " is the Winner").encode())
        """