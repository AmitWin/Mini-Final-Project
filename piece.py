import pygame as pg

blackColor = [0, 0, 0]
whiteColor = [255, 255, 255]

class Piece():
    def __init__(self, location, sqr_width, sqr_height):
        self.radius = 30
        self.black = False
        self.white = False
        self.sqr_width = sqr_width
        self.sqr_height = sqr_height
        self.boardLocation = location
        self.adjust_location(location)

    def adjust_location(self, location):
        self.location = [0.5 * self.sqr_height + location[1] * self.sqr_height, self.sqr_width * 0.5 + location[0] * self.sqr_width]
        self.location[0] = int(self.location[0])
        self.location[1] = int(self.location[1])

    def draw(self, win):
        if self.black:
            pg.draw.circle(win, blackColor, self.location, self.radius)
        elif self.white:
            pg.draw.circle(win, whiteColor, self.location, self.radius)

    def clicked(self, mousePos):
        dist = ((mousePos[0] - self.location[0]) ^ 2 + (mousePos[1] - self.location[1]) ^ 2) ^ 0.5
        if dist < self.radius:
            return True
        return False