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
        self.board = [[],
                      [],
                      [],
                      [],
                      [],
                      [],
                      [],
                      []]

    def draw(self, win):
        for i in range(self.rows):
            for j in range(self.cols):
                if (i + j) % 2 == 0:
                    pg.draw.rect(win, yellow, (self.sqr_width * i, self.sqr_height * j, self.sqr_width, self.sqr_height))
                elif (i + j) % 2 == 1:
                    pg.draw.rect(win, blue, (self.sqr_width * i, self.sqr_height * j, self.sqr_width, self.sqr_height))
