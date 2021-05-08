import pygame as pg
from board import Board
from info import boardWidth, boardHeight, clicked, win

board = Board()


def ValidClicked(mousePos, currentPlayer):
    for rowPieces in board.board:
        for piece in rowPieces:
            if piece != 0:
                if currentPlayer == 1 and piece.white:
                    if clicked(piece.position, mousePos):
                        return piece
                elif currentPlayer == -1 and piece.black:
                    if clicked(piece.position, mousePos):
                        return piece
    return False


def RedrawGameWindow():
    board.draw()
    for rowPieces in board.board:
        for piece in rowPieces:
            if piece != 0:
                piece.draw()
    pg.display.update()


# Main Loop
def main():
    run = True
    clock = pg.time.Clock()
    board.initiateBoard()
    currentPlayer = 1
    RedrawGameWindow()

    while run:
        clock.tick(27)

        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                run = False

            if event.type == pg.MOUSEBUTTONDOWN:
                mousePos = pg.mouse.get_pos()
                clickedPiece = ValidClicked(mousePos, currentPlayer)
                while clickedPiece:
                    board.update_moves(clickedPiece)
                    clickedPiece = board.move(clickedPiece)
                    if clickedPiece == "moved":
                        currentPlayer *= -1
                        clickedPiece = None

                    RedrawGameWindow()




main()
