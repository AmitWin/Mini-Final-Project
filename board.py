import pygame as pg
from piece import Piece
from info import yellow, blue, sqr_height, sqr_width, rows, cols, radius, adjust_location, clicked, adjust_position
import time


class Board():
    def __init__(self):
        self.board = []

        self.ready = False
        self.last = None
        self.copy = True

        self.p1Name = "Player 1"
        self.p2Name = "Player 2"

        self.turn = "w"

        self.time1 = 300
        self.time2 = 300
        self.startTime = time.time()

        self.winner = None

        self.start_user = None

    def initiateBoard(self):
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

    def draw(self, win):
        for i in range(rows):
            for j in range(cols):
                if (i + j) % 2 == 0:
                    pg.draw.rect(win, yellow, (sqr_width * i, sqr_height * j, sqr_width, sqr_height))
                elif (i + j) % 2 == 1:
                    pg.draw.rect(win, blue, (sqr_width * i, sqr_height * j, sqr_width, sqr_height))

    def update_moves(self, piece):
        checker = lambda x, y: 0 <= x + y < 8
        piece.possibleLocations = []
        column, row = piece.col, piece.row
        if self.board[row][column] != 0:
            vectors = [[1, -1], [1, 1]] if self.board[row][column].black else [[-1, -1], [-1, 1]]
            if self.board[row][column].queen:
                vectors = [[1, -1], [1, 1], [-1, -1], [-1, 1]]
            for vector in vectors:
                rowVector, columnVector = vector
                if checker(columnVector, column) and checker(rowVector, row):
                    if self.board[row + rowVector][column + columnVector] == 0:
                        piece.possibleLocations.append([row + rowVector, columnVector + column])
                    elif self.board[row + rowVector][column + columnVector] != 0 and \
                            self.board[row + rowVector][column + columnVector].white != self.board[row][column].white:
                        if checker((2 * columnVector), column) and checker((2 * rowVector), row) \
                                and self.board[2 * rowVector + row][2 * columnVector + column] == 0:
                            piece.possibleLocations.append([2 * rowVector + row, 2 * columnVector + column])

    def select(self, row, col):
        return self.move(self.board[row][col])

    def move(self, piece, win):
        pressed = False
        while not pressed:
            piece.highlight_possible_location(win)

            keys = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                    run = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    mousePos = pg.mouse.get_pos()
                    mouseLoc = adjust_position(mousePos)
                    if mouseLoc in piece.possibleLocations:
                        self.board[piece.row][piece.col] = 0

                        if abs(mouseLoc[0] - piece.row) == 2 or abs(mouseLoc[1] - piece.col) == 2:
                            self.board[(mouseLoc[0] + piece.row) // 2][(mouseLoc[1] + piece.col) // 2] = 0

                        self.update_location(piece, mouseLoc)
                        piece.checks_if_become_queen()

                        return "moved"
                    elif self.board[mouseLoc[0]][mouseLoc[1]] != 0 \
                            and self.board[mouseLoc[0]][mouseLoc[1]].white == piece.white:
                        return self.board[mouseLoc[0]][mouseLoc[1]]
                    pressed = True

        piece.possibleLocations = []
        return None

    def update_location(self, piece, location):
        self.board[location[0]][location[1]] = piece
        piece.change_pos(location)

    def checks_if_someone_won(self):
        black = 0
        white = 0
        for row in rows:
            for col in cols:
                if self.board[row][col].white:
                    white += 1
                elif self.board[row][col].black:
                    black += 1

        if black == 0:
            self.winner = "w"
            return True
        elif white == 0:
            self.winner = "b"
            return True

        return False
