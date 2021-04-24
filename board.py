import pygame as pg

black = [0, 0, 0]
white = [255, 228, 196]


class Board():
    def __init__(self):
        self.width = 800
        self.height = 800
        self.rows = 8
        self.cols = 8
        self.sqr_width = self.width / self.rows
        self.sqr_height = self.height / self.cols
        #self.board =

    def draw(self, win):
        for i in range(self.rows):
            for j in range(self.cols):
                if (i + j) % 2 == 0:
                    pg.draw.rect(win, black, (self.sqr_width * i, self.sqr_height * j, self.sqr_width, self.sqr_height))
                elif (i + j) % 2 == 1:
                    pg.draw.rect(win, white, (self.sqr_width * i, self.sqr_height * j, self.sqr_width, self.sqr_height))
