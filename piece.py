import pygame as pg
from info import black, white, radius, sqr_width, sqr_height, adjust_location, clicked, rows


class Piece():
    def __init__(self, location, isBlack):
        self.black = isBlack
        self.white = not isBlack
        self.queen = False
        self.possibleLocations = []
        self.row = location[0]
        self.col = location[1]
        self.position = adjust_location(location)

    def draw(self, win):
        if self.black:
            if not self.queen:
                pg.draw.circle(win, black, self.position, radius)
            else:
                pg.draw.circle(win, black, self.position, radius, 10)

        elif self.white:
            if not self.queen:
                pg.draw.circle(win, white, self.position, radius)
            else:
                pg.draw.circle(win, white, self.position, radius, 10)

    def change_pos(self, location):
        self.row = location[0]
        self.col = location[1]
        self.position = adjust_location(location)

    def __str__(self):
        return str(self.col) + " " + str(self.row)

    def highlight_possible_location(self, win):
        for possibleLocation in self.possibleLocations:
            pos = adjust_location(possibleLocation)
            pg.draw.circle(win, (2, 28, 30), pos, radius)
        pg.display.update()

    def checks_if_become_queen(self):
        if self.white and self.row == 0:
            self.queen = True

        elif self.black and self.row == rows - 1:
            self.queen = True
