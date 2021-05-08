import pygame as pg
from board import Board
from info import boardWidth, boardHeight, clicked, win
from client import Client
import time
import pickle
import os
pg.font.init()

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


def RedrawGameWindow(game, p):
    win.fill((128, 128, 128))
    if not game.connected():
        font = pg.font.SysFont('comicsans', 80)
        text = font.render('Waiting for player...', 1, (255, 0, 0), True)
        win.blit(text, (boardWidth // 2 - text.get_width() // 2, boardHeight // 2 - text.get_height() // 2))

    board.draw()
    for rowPieces in board.board:
        for piece in rowPieces:
            if piece != 0:
                piece.draw()
    pg.display.update()


# Main Loop
def main():
    run = True
    turn = "w"
    clock = pg.time.Clock()
    board.initiateBoard()
    n = Client()
    currentPlayer = int(n.getP())

    while run:
        clock.tick(27)

        try:
            game = n.send("get")
        except:
            run = False
            print("couldn't get game")
            break

        

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
                    if not clickedPiece:
                        n.send(board.board)

                    RedrawGameWindow(game, currentPlayer)
        RedrawGameWindow(game, currentPlayer)


main()
