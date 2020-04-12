import socket
from Objects import *
import pygame
import pickle
from Network import *

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic Tac Toe')
n = Network()

player = n.p
n.send("connection made")
pygame.init()
def main():
    global win, n, player
    text = ("Winner", "Loser", "Draw")
    game = pickle.loads(n.recv())
    run = True
    while run:
        pygame.display.update()
        game.draw(win)
        if game.ready and game.win_player == '' and game.players[player-1].turn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rum = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for rect in game.rectangles:
                        if rect.isclicked(pos):
                            n.send(str.encode(str(rect.index)))
                            game = n.recv()
                            break
        elif game.win_player in (1, 2, 3):
            run = False
            if player == game.win_player:
                win.blit(text[0], (250, 250))
            elif player != 3:
                win.blit(text[1], (250, 250))
            else:
                win.blit(text[3], (250, 250))
        else:
            win.blit("Waiting for player", (250, 250))


main()