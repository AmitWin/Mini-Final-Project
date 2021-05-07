import pygame as pg

# Board Information
boardWidth = 600
boardHeight = 600
rows = 8
cols = 8
sqr_width = boardWidth / rows
sqr_height = boardHeight / cols

# Initiate Windows
win = pg.display.set_mode((boardWidth, boardHeight))
pg.display.set_caption("Checkers")

# Colors
black = [0, 0, 0]
white = [255, 255, 255]
yellow = [154, 205, 50]
blue = [65, 105, 225]

# Piece Information
radius = int(3 * sqr_width / 8)


# Adjust board location to mouse position and the opposite
def adjust_location(location):
    position = [0.5 * sqr_height + location[1] * sqr_height, sqr_width * 0.5 + location[0] * sqr_width]
    position[0] = int(position[0])
    position[1] = int(position[1])
    return position

def adjust_position(position):
    location = [position[1] // sqr_height, position[0] // sqr_width]
    location[0] = int(location[0])
    location[1] = int(location[1])
    return location


# Checks if a circle was clicked
def clicked(position, mousePos):
    dist = ((mousePos[0] - position[0]) ** 2 + (mousePos[1] - position[1]) ** 2) ** 0.5
    if dist < radius:
        return True
    return False
