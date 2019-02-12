import pygame
import colors
import string
import utilities
from typing import Tuple

NBLOCKS = 11


class GameBoard(pygame.sprite.Sprite):
    """
    The Game Board is a 10x10 grid of spaces which may contain sprite images
    Columns are indexed by number [0-9] and rows are indexed by letter [A-J]

          0|1|2|3|4|5|6|7|8|9|
        A|_|_|_|_|_|_|_|_|_|_|
        B|_|_|_|_|_|_|_|_|_|_|
        C|_|_|_|_|_|_|_|_|_|_|
        D|_|_|_|_|_|_|_|_|_|_|
        E|_|_|_|_|_|_|_|_|_|_|
        F|_|_|_|_|_|_|_|_|_|_|
        G|_|_|_|_|_|_|_|_|_|_|
        H|_|_|_|_|_|_|_|_|_|_|
        I|_|_|_|_|_|_|_|_|_|_|
        J|_|_|_|_|_|_|_|_|_|_|

    """
    def __init__(self, dimension):
        super().__init__()
        self.image = pygame.Surface(dimension)
        self.image.convert()
        self.rect = self.image.get_rect()

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # helper variables for spacing sprite images
        self.x_step = self.width // NBLOCKS
        self.y_step = self.height // NBLOCKS


    def refresh(self):
        # Draw board background use color [board_bkgd]
        self.image.fill(colors.board_bkgd)

        # --------- BEGIN YOUR CODE ----------

        # Draw row and column header backgrounds
        #   Headers should be 1 block wide/tall and use color [header]
        pygame.draw.rect(self.image, colors.header, (0, 0, self.x_step, self.height))
        pygame.draw.rect(self.image, colors.header, (0, 0, self.width, self.y_step))


        # Draw grid lines use color [foreground]
        for n in range(1,NBLOCKS):
            pygame.draw.line(self.image, colors.foreground, (self.x_step*n, 0), (self.x_step*n, self.height))
            pygame.draw.line(self.image, colors.foreground, (0, self.x_step * n), (self.width, self.y_step * n))


        # Draw row labels [A-J] centered in each header block
        #    use color [foreground] and font [
        letters = 'A B C D E F G H I J'.split(' ')
        for n in range(1,NBLOCKS):
            text = utilities.create_text(letters[n-1], 24, colors.foreground)
            textRect = text.get_rect()
            textRect.centerx = self.x_step/2
            textRect.centery = self.y_step/2 +self.y_step*n
            self.image.blit(text, textRect)


        # Draw column labels [0-9] centered in each header block
        #    use color [foreground]
        for n in range(1,NBLOCKS):
            text = utilities.create_text(str(n-1), 24, colors.foreground)
            textRect = text.get_rect()
            textRect.centerx = self.x_step/2 +self.x_step*n
            textRect.centery = self.y_step/2
            self.image.blit(text, textRect)


        # Draw border around the board use color [foreground]
        pygame.draw.line(self.image, colors.foreground, (0, 0), (self.width, 0))
        pygame.draw.line(self.image, colors.foreground, (self.width-1, 0), (self.width-1, self.height))
        pygame.draw.line(self.image, colors.foreground, (self.width, self.height-1), (0, self.height-1))
        pygame.draw.line(self.image, colors.foreground, (0, self.height), (0, 0))
        # --------- END YOUR CODE ------------

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def add_sprite(self, sprite: pygame.Surface, loc: Tuple[int, int]):
        """
        Place a sprite on the game board in location (row,col)
        """
        row = loc[0]
        col = loc[1]
        x = self.x_step * (col + 1)
        y = self.y_step * (row + 1)
        self.image.blit(sprite, (x, y))
