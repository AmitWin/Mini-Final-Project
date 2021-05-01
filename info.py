import pygame as pg

# Board Information
boardWidth = 600
boardHeight = 600
rows = 8
cols = 8
sqr_width = boardWidth / rows
sqr_height = boardHeight / cols

# Colors
black = [0, 0, 0]
white = [255, 255, 255]
yellow = [154, 205, 50]
blue = [65, 105, 225]

# Piece Information
radius = int(3 * sqr_width / 8)