import pygame as pg

blackColor = [0, 0, 0]
whiteColor = [255, 255, 255]

class Piece():
    def __init__(self, location):
        self.diameter = 70
        self.black = False
        self.white = False
        self.location = location

    def draw(self, win):
        if self.black:
            pg.draw.circle(win, blackColor, self.location, self.diameter)
        elif self.white:
            pg.draw.circle(win, blackColor, self.location, self.diameter)