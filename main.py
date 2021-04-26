import pygame as pg
from board import Board

board = Board()

win = pg.display.set_mode((board.width, board.height))
pg.display.set_caption("Checkers")


def draw():
    board.draw(win)
    for blackPiece in board.blackPieces:
        blackPiece.draw(win)
    for whitePiece in board.whitePieces:
        whitePiece.draw(win)
    pg.display.update()

#Main Loop
def main():
    run = True
    clock = pg.time.Clock()
    board.initiateBoard()

    while run:
        clock.tick(27)

        keys = pg.key.get_pressed()
        for e in pg.event.get():
            if e.type == pg.QUIT or keys[pg.K_ESCAPE]:
                run = False

            if e.type == pg.MOUSEBUTTONDOWN:
                pass

        draw()

main()
