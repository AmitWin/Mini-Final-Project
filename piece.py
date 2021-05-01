import pygame as pg
from info import black, white, radius, sqr_width, sqr_height

class Piece():
    def __init__(self, location, isBlack):
        self.black = isBlack
        self.white = not isBlack
        self.queen = False
        self.row = location[0]
        self.col = location[1]
        self.adjust_location(location)
        self.possibleLocations = []

    def adjust_location(self, location):
        self.position = [0.5 * sqr_height + location[1] * sqr_height, sqr_width * 0.5 + location[0] * sqr_width]
        self.position[0] = int(self.position[0])
        self.position[1] = int(self.position[1])

    def draw(self, win):
        if self.black:
            pg.draw.circle(win, black, self.position, radius)
        elif self.white:
            pg.draw.circle(win, white, self.position, radius)

    def clicked(self, mousePos):
        dist = ((mousePos[0] - self.position[0]) ** 2 + (mousePos[1] - self.position[1]) ** 2) ** 0.5
        if dist < radius:
            return True
        return False