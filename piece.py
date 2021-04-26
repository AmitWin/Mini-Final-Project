import pygame as pg

blackColor = [0, 0, 0]
whiteColor = [255, 255, 255]

class Piece():
    def __init__(self, location, sqr_width, sqr_height):
        self.diameter = 30
        self.black = False
        self.white = False
        self.sqr_width = sqr_width
        self.sqr_height = sqr_height
        self.location = (0.5*sqr_height + location[1]*sqr_height, sqr_width*0.5 + location[0]*sqr_width)


    def draw(self, win):
        if self.black:
            pg.draw.circle(win, blackColor, self.location, self.diameter)
        elif self.white:
            pg.draw.circle(win, whiteColor, self.location, self.diameter)