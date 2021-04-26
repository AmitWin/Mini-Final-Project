import pygame as pg
from piece import Piece

yellow = [154, 205, 50]
blue = [65, 105, 225]


class Board():
    def __init__(self):
        self.width = 600
        self.height = 600
        self.rows = 8
        self.cols = 8
        self.sqr_width = self.width / self.rows
        self.sqr_height = self.height / self.cols
        self.board = None

    def initiateBoard(self):
        self.blackPieces = []
        self.whitePieces = []
        for i in range(3):
            for j in range(4):
                if i % 2 == 0:
                    piece = Piece([i, 1 + j*2], self.sqr_width, self.sqr_height)
                else:
                    piece = Piece([i, j*2], self.sqr_width, self.sqr_height)
                piece.black = True
                self.blackPieces.append(piece)

        for i in range(3):
            for j in range(4):
                if i % 2 == 0:
                    piece = Piece([self.rows - i - 1, j*2], self.sqr_width, self.sqr_height)
                else:
                    piece = Piece([self.rows - i - 1, 1 + j*2], self.sqr_width, self.sqr_height)
                piece.white = True
                self.whitePieces.append(piece)


    def draw(self, win):
        for i in range(self.rows):
            for j in range(self.cols):
                if (i + j) % 2 == 0:
                    pg.draw.rect(win, yellow, (self.sqr_width * i, self.sqr_height * j, self.sqr_width, self.sqr_height))
                elif (i + j) % 2 == 1:
                    pg.draw.rect(win, blue, (self.sqr_width * i, self.sqr_height * j, self.sqr_width, self.sqr_height))
