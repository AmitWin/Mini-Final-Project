import pygame as pg
from board import Board
from info import boardWidth, boardHeight

board = Board()

win = pg.display.set_mode((boardWidth, boardHeight))
pg.display.set_caption("Checkers")

def ValidClicked(mousePos, currentPlayer):
    for rowPieces in board.board:
        for piece in rowPieces:
            if piece != 0:
                if currentPlayer == 1 and piece.white:
                    if piece.clicked(mousePos):
                        return piece
                elif currentPlayer == -1 and piece.black:
                    if piece.clicked(mousePos):
                        return piece
    return False

def RedrawGameWindow():
    board.draw(win)
    for rowPieces in board.board:
        for piece in rowPieces:
            if piece != 0:
                piece.draw(win)
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
                    clickedPiece = ValidClicked(mousePos, currentPlayer)
                    if clickedPiece:
                        board.PossibleLocation(clickedPiece)
                        print(clickedPiece.possibleLocations)
                elif currentPlayer == -1:
                    pass

        RedrawGameWindow()

main()
