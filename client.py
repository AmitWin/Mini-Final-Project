import socket
import pickle
import time
from checkers import *
import threading
from board import Board
import pygame as pg
from info import boardWidth, boardHeight


class Client(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 5555
        self.addr = (self.host, self.port)
        self.color = None
        self.board = None

    def run(self):
        self.connect()
        self.connect_to_lobby()

    def connect_to_lobby(self):
        # safety!!
        lobbyId = input("Do you want to Create lobby or Join one (C, J)")
        if lobbyId == "C":
            self.server.send(b"-1")
        elif lobbyId == "J":
            lobbyId = input("Enter id number")
            self.server.send(lobbyId.encode())

        data = self.server.recv(1024).decode()
        if "Creating New Lobby" in data:
            print(data)
        elif data == "Joining Into an Existing Lobby":
            print(data)

        self.play()

    def play(self):
        global board, turn, currentPlayer
        self.server.recv(1024)  # Received that game started

        color = self.server.recv(1024).decode()
        self.color = color.split(":")[-1]
        currentPlayer = 1 if self.color == "w" else -1

        if self.color == "w":
            turn = True
        else:
            board = self.server.recv(1024 * 32)
            board = pickle.loads(board)
            turn = True

        while True:
            if not turn:
                newBoard = pickle.dumps(board)
                self.server.send(newBoard)
                board = self.server.recv(1024 * 32)
                board = pickle.loads(board)
                turn = True

        """
        board = self.server.recv(1024 * 32)
        self.board = pickle.loads(board)

        while not self.board.winner:
            turn = self.server.recv(1024).decode()
            turn = turn.decode()
            turn = turn.split(" ")[2]
            if turn == self.color:
                board = self.server.recv(1024 * 32)
                board = pickle.loads(board)
                #playing
                board = pickle.dumps(board)
                self.server.send(board)
        """

    def connect(self):
        try:
            self.server.connect(self.addr)
        except:
            print("Basasa")

    def disconnect(self):
        self.server.close()


def main():
    client = Client()
    client.start()

    # Initiate Windows
    win = pg.display.set_mode((boardWidth, boardHeight))
    pg.display.set_caption("Checkers")

    global turn, board, currentPlayer
    board = Board()
    turn = False
    run = True
    clock = pg.time.Clock()
    while run:
        clock.tick(27)

        RedrawGameWindow(board, win)

        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                run = False

            if turn:
                if event.type == pg.MOUSEBUTTONDOWN:
                    mousePos = pg.mouse.get_pos()
                    clickedPiece = ValidClicked(mousePos, currentPlayer)
                    while clickedPiece:
                        board.update_moves(clickedPiece)
                        clickedPiece = board.move(clickedPiece, win)
                        if clickedPiece == "moved":
                            turn = False
                            clickedPiece = None

                        RedrawGameWindow(board, win)
    pg.quit()


if __name__ == '__main__':
    if __name__ == '__main__':
        if __name__ == '__main__':
            main()
