import pygame as pg
from board import Board
from info import boardWidth, boardHeight, clicked, win
from client import Client
import time
import pickle
import os

pg.font.init()

turn = "w"


def ValidClicked(mousePos, color):
    for rowPieces in board.board:
        for piece in rowPieces:
            if piece != 0:
                if color == "w" and piece.white:
                    if clicked(piece.position, mousePos):
                        return piece
                elif color == "b" and piece.black:
                    if clicked(piece.position, mousePos):
                        return piece
    return False


def RedrawGameWindow(p1time, p2time, color, ready):
    win.fill((128, 128, 128))

    board.draw()

    for rowPieces in board.board:
        for piece in rowPieces:
            if piece != 0:
                piece.draw()

    formatTime1 = str(int(p1time // 60)) + ":" + str(int(p1time % 60))
    formatTime2 = str(int(p2time // 60)) + ":" + str(int(p2time % 60))
    if int(p1time % 60) < 10:
        formatTime1 = formatTime1[:-1] + "0" + formatTime1[-1]
    if int(p2time % 60) < 10:
        formatTime2 = formatTime2[:-1] + "0" + formatTime2[-1]

    font = pg.font.SysFont("comicsans", 30)
    try:
        txt = font.render(board.p1Name + "\'s Time: " + str(formatTime2), 1, (255, 255, 255))
        txt2 = font.render(board.p2Name + "\'s Time: " + str(formatTime1), 1, (255, 255, 255))
    except Exception as e:
        print(e)

    win.blit(txt, (520, 10))
    win.blit(txt2, (520, 700))

    txt = font.render("Press q to Quit", 1, (255, 255, 255))
    win.blit(txt, (10, 20))

    if not ready:
        show = "Waiting for Player"
        font = pg.font.SysFont("comicsans", 80)
        txt = font.render(show, 1, (255, 0, 0))
        win.blit(txt, (boardWidth / 2 - txt.get_width() / 2, 300))

    font = pg.font.SysFont("comicsans", 30)
    if color == "w":
        txt3 = font.render("YOU ARE WHITE", 1, (255, 0, 0))
        win.blit(txt3, (boardWidth / 2 - txt3.get_width() / 2, 10))
    else:
        txt3 = font.render("YOU ARE BLACK", 1, (255, 0, 0))
        win.blit(txt3, (boardWidth / 2 - txt3.get_width() / 2, 10))

    if board.turn == color:
        txt3 = font.render("YOUR TURN", 1, (255, 0, 0))
        win.blit(txt3, (boardWidth / 2 - txt3.get_width() / 2, 700))
    else:
        txt3 = font.render("THEIR TURN", 1, (255, 0, 0))
        win.blit(txt3, (boardWidth / 2 - txt3.get_width() / 2, 700))

    pg.display.update()


def end_screen(text):
    pg.font.init()
    font = pg.font.SysFont("comicsans", 80)
    txt = font.render(text, 1, (255, 0, 0))
    win.blit(txt, (boardWidth / 2 - txt.get_width() / 2, 300))
    pg.display.update()

    pg.time.set_timer(pg.USEREVENT + 1, 3000)

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                run = False
            elif event.type == pg.KEYDOWN:
                run = False
            elif event.type == pg.USEREVENT + 1:
                run = False


def connect():
    global c
    c = Client()
    return c.board


# Main Loop
def main():
    global turn, board, name

    color = board.start_user
    count = 0

    board = c.send("update_moves")
    board = c.send("name " + name)
    clock = pg.time.Clock()
    run = True

    board.initiateBoard()

    while run:

        p1Time = board.time1
        p2Time = board.time2
        if count == 60:
            board = c.send("get")
            count = 0
        else:
            count += 1
            clock.tick(27)

        try:
            RedrawGameWindow(p1Time, p2Time, color, board.ready)
        except Exception as e:
            print(e)
            end_screen("Other player left")
            run = False
            break

        if p1Time <= 0:
            board = c.send("winner b")
        elif p2Time <= 0:
            board = c.send("winner w")

        if board.winner == "w":
            end_screen("White is the Winner!")
            run = False
        elif board.winner == "b":
            end_screen("Black is the Winner!")
            run = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                quit()
                pg.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    if color == "w":
                        board = c.send("winner b")
                    elif color == "b":
                        board = c.send("winner w")

            if event.type == pg.MOUSEBUTTONDOWN:
                if color == board.turn and board.ready:
                    mousePos = pg.mouse.get_pos()
                    clickedPiece = ValidClicked(mousePos, color)
                    while clickedPiece:
                        board = c.send("update moves")
                        board = c.send("select " + str(clickedPiece.row) + " " + str(clickedPiece.col))

                    """
                    clickedPiece = ValidClicked(mousePos, currentPlayer)
                    while clickedPiece:
                        board.update_moves(clickedPiece)
                        clickedPiece = board.move(clickedPiece)
                        if not clickedPiece:
                            n.send(board.board)

                        RedrawGameWindow(game, currentPlayer)
                    """

    c.disconnect()
    board = 0

try:
    bo = connect()
    main()
except:
    print("Server Offline")

name = input("Please type your name: ")
