import pygame
from pygame.locals import *
import sys

import colors
import sprites
from time import sleep

import human
import computer
from game_board import GameBoard
import utilities

BLOCK_SIZE = 30
NBLOCKS = 11
TOP_MARGIN = 30
PADDING = 10


def main():
    pygame.init()

    screen: pygame.Surface = pygame.display.set_mode(((BLOCK_SIZE * NBLOCKS) * 2 + PADDING * 3,
                                                      BLOCK_SIZE * NBLOCKS + TOP_MARGIN + PADDING))
    screen.fill(colors.screen_bkgd)
    pygame.display.set_caption('USNA Battleship')
    sprites.initialize()

    # size of the game board figure based on BLOCK SIZE pixels
    board_dimension = (BLOCK_SIZE * NBLOCKS, BLOCK_SIZE * NBLOCKS)

    # "my" game board has my ships
    my_board: GameBoard = GameBoard(board_dimension)
    my_board.rect.top = TOP_MARGIN
    my_board.rect.left = PADDING

    # "their" game board has my guesses
    their_board: GameBoard = GameBoard(board_dimension)
    # position their_board PADDING pixels to the right of my_board
    their_board.rect.top = TOP_MARGIN
    their_board.rect.left = PADDING * 2 + my_board.rect.width

    # paint the board surface
    my_board.refresh()
    their_board.refresh()

    # --------- BEGIN YOUR CODE ----------
    # add titles above the game boards
    # draw 'YOU' centered above my_board
    you = utilities.create_text('YOU', 24, colors.foreground)
    youRect = you.get_rect()
    youRect.centerx = PADDING + (BLOCK_SIZE * NBLOCKS) / 2
    youRect.centery = TOP_MARGIN / 2
    screen.blit(you, youRect)

    # draw 'THEM' centered above their_board
    them = utilities.create_text('THEM', 24, colors.foreground)
    themRect = them.get_rect()
    themRect.centerx = PADDING * 2 + (BLOCK_SIZE * NBLOCKS) * 1.5
    themRect.centery = TOP_MARGIN / 2
    screen.blit(them, themRect)
    # --------- END YOUR CODE ------------

    # create a human player
    # player1 = human.Human()
    player1 = computer.Computer()
    player1.initialize()
    player1.draw(my_board, their_board)

    # create a computer player
    player2 = computer.Computer()
    player2.initialize()

    # place the board on the screen
    their_board.draw(screen)
    my_board.draw(screen)
    pygame.display.update()


    # play the game until one of the players is complete
    while not player1.complete and not player2.complete:

        # player1's turn
        player1.take_turn(player2)
        player1.draw(my_board, their_board)
        my_board.draw(screen)
        their_board.draw(screen)
        pygame.display.update()

        # player2's turn
        player2.take_turn(player1)
        # note: we always draw player1's board, why?
        player1.draw(my_board, their_board)
        my_board.draw(screen)
        their_board.draw(screen)
        pygame.display.update()

        # process event queue, quit if user clicks 'X' button
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    # display the winner
    if player1.complete and not player2.complete:
        _display_message(screen, "You Win!")

    elif player2.complete and not player1.complete:
        _display_message(screen, "You Lose!")
    else:
        _display_message(screen, "Tie Game!")

    # wait until the user closes the game
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


def _display_message(screen: pygame.Surface, msg: str):
    """
    Display [msg] in the message box sprite in the center of the screen
    """

    # make a copy of the msg_box sprite because we need to edit it
    box = sprites.msg_box.copy()

    # --------- BEGIN YOUR CODE ----------

    # create a text object with size 42 font of [msg]
    endGame = utilities.create_text(msg, 42, colors.foreground)
    endRect = endGame.get_rect()
    endRect.centerx = 125
    endRect.centery = 61
    # blit the text onto the box surface
    box.blit(endGame, endRect)
    # blit the box onto the center of the screen
    screen.blit(box, (((BLOCK_SIZE * NBLOCKS) * 2 + PADDING * 3)/2-125, (BLOCK_SIZE * NBLOCKS + TOP_MARGIN + PADDING)/2-61))
    pygame.display.update()
    # remove this once you have implemented the drawing code
    print(msg)

    # --------- BEGIN YOUR CODE ----------


main()
