import pygame as pg
from board import Board
from info import boardWidth, boardHeight, clicked

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


def RedrawGameWindow(board, win):
    board.draw(win)
    for rowPieces in board.board:
        for piece in rowPieces:
            if piece != 0:
                piece.draw(win)
    pg.display.update()

# Main Loop
def main():
    # Initiate Windows
    win = pg.display.set_mode((boardWidth, boardHeight))
    pg.display.set_caption("Checkers")

    run = True
    clock = pg.time.Clock()
    currentPlayer = 1
    RedrawGameWindow(board, win)

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
                    clickedPiece = board.move(clickedPiece, win)
                    if clickedPiece == "moved":
                        currentPlayer *= -1
                        clickedPiece = None

                    RedrawGameWindow(board, win)

if __name__ == '__main__':
    if __name__ == '__main__':
        main()
