import pygame as pg
from info import black, white, radius, sqr_width, sqr_height, adjust_location, clicked, win

class Piece():
    def __init__(self, location, isBlack):
        self.black = isBlack
        self.white = not isBlack
        self.queen = False
        self.row = location[0]
        self.col = location[1]
        self.possibleLocations = []
        self.position = adjust_location(location)

    def draw(self):
        if self.black:
            pg.draw.circle(win, black, self.position, radius)
        elif self.white:
            pg.draw.circle(win, white, self.position, radius)