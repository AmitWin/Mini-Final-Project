import pygame as pg
from board import Board

board = Board()

win = pg.display.set_mode((board.width, board.height))
pg.display.set_caption("Checkers")


def RedrawGameWindow():
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
    currentPlayer = 1

    while run:
        clock.tick(27)

        keys = pg.key.get_pressed()
        for e in pg.event.get():
            if e.type == pg.QUIT or keys[pg.K_ESCAPE]:
                run = False

            if e.type == pg.MOUSEBUTTONDOWN:
                mousePos = pg.mouse.get_pos()
                if currentPlayer == 1:
                    for whitePiece in board.whitePieces:
                        if whitePiece.clicked(mousePos):
                            pass
                elif currentPlayer == -1:
                    pass

        RedrawGameWindow()

main()
