import pygame as pg
from piece import Piece
from info import yellow, blue, sqr_height, sqr_width, rows, cols, radius

class Board():
    def __init__(self):
        self.board = []

    def initiateBoard(self):
        for row in range(rows):
            self.board.append([])
            for col in range(cols):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece([row, col], True))
                    elif row > 4:
                        self.board[row].append(Piece([row, col], False))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.win = win
        for i in range(rows):
            for j in range(cols):
                if (i + j) % 2 == 0:
                    pg.draw.rect(win, yellow, (sqr_width * i, sqr_height * j, sqr_width, sqr_height))
                elif (i + j) % 2 == 1:
                    pg.draw.rect(win, blue, (sqr_width * i, sqr_height * j, sqr_width, sqr_height))

    def PossibleLocation(self, piece):
        if piece.white:
            if not piece.queen:
                if piece.row < rows - 1:
                    if 0 < piece.col:
                        possibleLocation = self.board[piece.row - 1][piece.col - 1]
                        if possibleLocation == 0:
                            piece.possibleLocations.append([piece.row - 1, piece.col - 1])
                        elif possibleLocation.black:
                            if piece.row + 2 >= 0 and piece.col - 2 >= 0:
                                if self.board[piece.row - 2, piece.col -2] == 0:
                                    piece.possibleLocations.append([piece.row - 2, piece.col -2])
                    if piece.col < cols - 1:
                        possibleLocation = self.board[piece.row - 1][piece.col + 1]
                        if possibleLocation == 0:
                            piece.possibleLocations.append([piece.row - 1, piece.col + 1])
                        elif possibleLocation.black:
                            if piece.row - 2 <= 0 and piece.col + 2 <= 0:
                                if self.board[piece.row - 2][piece.col + 2] == 0:
                                    piece.possibleLocations.append([piece.row - 2, piece.col + 2])

        if piece.black:
            if not piece.queen:
                if piece.row > 0:
                    if 0 < piece.col:
                        possibleLocation = self.board[piece.row + 1, piece.col - 1]
                        if possibleLocation == 0:
                            piece.possibleLocations.append([piece.row + 1, piece.col - 1])
                        elif possibleLocation.black:
                            if piece.row + 2 >= 0 and piece.col - 2 >= 0:
                                if self.board[piece.row + 2, piece.col -2] == 0:
                                    piece.possibleLocations.append([piece.row + 2, piece.col -2])
                    if piece.col < cols - 1:
                        possibleLocation = self.board[piece.row + 1, piece.col + 1]
                        if possibleLocation == 0:
                            piece.possibleLocations.append([piece.row + 1, piece.col + 1])
                        elif possibleLocation.black:
                            if piece.row + 2 <= 0 and piece.col + 2 <= 0:
                                if self.board[piece.row + 2, piece.col + 2] == 0:
                                    piece.possibleLocations.append([piece.row + 2, piece.col + 2])

    def draw_possible_location(self, piece):
        for location in piece.possibleLocations:
            pg.draw.circle(self.win, black, self.position, radius)

