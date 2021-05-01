import pygame as pg
from piece import Piece
from info import yellow, blue, sqr_height, sqr_width, rows, cols, radius, adjust_location, clicked, win

class Board():
    def __init__(self):
        self.board = []

    def initiateBoard(self):
        """

        :return:
        """
        for row in range(rows):
            self.board.append([])
            for col in range(cols):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece([row, col], True))
                    elif row > 4:
                        self.board[row].append(Piece([row, col], False))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self):
        for i in range(rows):
            for j in range(cols):
                if (i + j) % 2 == 0:
                    pg.draw.rect(win, yellow, (sqr_width * i, sqr_height * j, sqr_width, sqr_height))
                elif (i + j) % 2 == 1:
                    pg.draw.rect(win, blue, (sqr_width * i, sqr_height * j, sqr_width, sqr_height))

    def PossibleLocation(self, piece):
        if piece.white:
            if not piece.queen:
                if piece.row >= 0:
                    if piece.col < cols - 1:
                        self.check_where_possible(piece, piece.row - 1, piece.col + 1, "right", "white")
                    if 0 < piece.col:
                        self.check_where_possible(piece, piece.row - 1, piece.col - 1, "left", "white")

        if piece.black:
            if not piece.queen:
                if piece.row < rows:
                    if 0 < piece.col:
                        self.check_where_possible(piece, piece.row + 1, piece.col + 1, "right", "black")
                    if piece.col < cols - 1:
                        self.check_where_possible(piece, piece.row + 1, piece.col - 1, "left", "black")

        pressed = False
        while not pressed:
            self.draw_possible_locations(piece)

            keys = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                    run = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    mousePos = pg.mouse.get_pos()
                    for location in piece.possibleLocations:
                        if clicked(adjust_location(location), mousePos):
                            self.board[piece.row][piece.col] = 0
                            pressed = True
                        elif clicked(piece.position, mousePos):
                            pressed = True

        piece.possibleLocations = []

    def check_where_possible(self, piece, row, col, direction, color):
        """
        The function checks which squares are available for the piece to go
        :param piece: the piece we want to move
        :param row: the row of the square we want to check if empty
        :param col: the col of the square we want to check if empty
        :param direction: right => 1, left => -1
        :param color: white => 1, black => -1
        :return: True if the piece ate another piece
        """
        ate = False
        dirc = 1 if direction == "right" else -1
        colour = 1 if color == "white" else -1
        possibleLocation = self.board[row][col]
        if possibleLocation == 0:
            piece.possibleLocations.append([row, col])
        elif possibleLocation.black:
            if piece.row + 2*colour >= 0 and piece.col + 2*dirc >= 0:
                if self.board[piece.row + 2*colour][piece.col + 2*dirc] == 0:
                    piece.possibleLocations.append([piece.row + 2*colour, piece.col + 2*dirc])
                    ate = True
        return ate

    def draw_possible_locations(self, piece):
        for possibleLocation in piece.possibleLocations:
            pos = adjust_location(possibleLocation)
            pg.draw.circle(win, (128, 128, 128), pos, radius)
        pg.display.update()

