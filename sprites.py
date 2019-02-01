import pygame

"""
 'cut out' sprites from the sprite sheet
 the first sprite is provided as an example
"""

# sprites are 30x30 tiles separated by 1 pixel margins
SPRITE_WIDTH = 30
SPRITE_HEIGHT = 30
SPRITE_MARGIN = 1

# an array of all the game sprites
sprites = []

# load the sprite sheet
sprite_sheet = pygame.image.load('assets/sprite_sheet.png')

# ---ship_top (30x30)---
#     create an empty surface for the sprite
ship_top = pygame.Surface((30, 30))
#     see blit documentation at
#     https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
ship_top.blit(sprite_sheet, (0, 0), pygame.Rect(0, 0, 30, 30))
#     add the sprite to the array
sprites.append(ship_top)

# --------- BEGIN YOUR CODE ----------

# ---ship_left (30x30)---
ship_left = pygame.Surface(SPRITE_WIDTH, SPRITE_HEIGHT)
ship_left.blit(sprite_sheet, (0, 0), pygame.Rect(SPRITE_WIDTH+SPRITE_MARGIN, 0, SPRITE_WIDTH*2+SPRITE_MARGIN, SPRITE_HEIGHT))
sprites.append(ship_left)

# ---ship_bottom (30x30)---
ship_bottom = pygame.Surface(SPRITE_WIDTH, SPRITE_HEIGHT)
ship_bottom.blit(sprite_sheet, (0, 0), pygame.Rect(SPRITE_WIDTH*2+SPRITE_MARGIN*2, 0, SPRITE_WIDTH*3+SPRITE_MARGIN*2, SPRITE_HEIGHT))
sprites.append(ship_bottom)

# ---ship_right (30x30)---
ship_right = pygame.Surface(SPRITE_WIDTH, SPRITE_HEIGHT)
ship_right.blit(sprite_sheet, (0, 0), pygame.Rect(SPRITE_WIDTH*3+SPRITE_MARGIN*3, 0,
                                                  SPRITE_WIDTH*4+SPRITE_MARGIN*3, SPRITE_HEIGHT))
sprites.append(ship_right)

# ---ship_horizontal (30x30)---
ship_horizontal = pygame.Surface((SPRITE_WIDTH, SPRITE_HEIGHT)
ship_horizontal.blit(sprite_sheet, (0, 0), pygame.Rect(0, SPRITE_HEIGHT+SPRITE_MARGIN, SPRITE_WIDTH, SPRITE_HEIGHT*2+SPRITE_MARGIN))
sprites.append(ship_horizontal)

# ---ship_vertical (30x30)---
ship_vertical = pygame.Surface((SPRITE_WIDTH, SPRITE_HEIGHT)
ship_vertical.blit(sprite_sheet, (0, 0), pygame.Rect(SPRITE_WIDTH+SPRITE_MARGIN, SPRITE_HEIGHT+SPRITE_MARGIN, SPRITE_WIDTH*2+SPRITE_MARGIN*1, SPRITE_HEIGHT*2+SPRITE_MARGIN))
sprites.append(ship_vertical)

# ---hit (30x30)---
ship_hit = pygame.Surface((SPRITE_WIDTH, SPRITE_HEIGHT)
ship_hit.blit(sprite_sheet, (0, 0), pygame.Rect(SPRITE_WIDTH*2+SPRITE_MARGIN*2, SPRITE_HEIGHT+SPRITE_MARGIN, SPRITE_WIDTH*3+SPRITE_MARGIN*2, SPRITE_HEIGHT*2+SPRITE_MARGIN))
sprites.append(ship_hit)

# ---miss (30x30)---
ship_miss = pygame.Surface((SPRITE_WIDTH, SPRITE_HEIGHT)
ship_miss.blit(sprite_sheet, (0, 0), pygame.Rect(SPRITE_WIDTH*3+SPRITE_MARGIN*3, SPRITE_HEIGHT+SPRITE_MARGIN, SPRITE_WIDTH*4+SPRITE_MARGIN*3, SPRITE_HEIGHT*2+SPRITE_MARGIN))
sprites.append(ship_miss)

# ---ship_sunk (30x30)---
ship_sunk = pygame.Surface((SPRITE_WIDTH, SPRITE_HEIGHT)
ship_sunk.blit(sprite_sheet, (0, 0), pygame.Rect(0, SPRITE_HEIGHT*2+SPRITE_MARGIN*2, SPRITE_WIDTH, SPRITE_HEIGHT*3+SPRITE_MARGIN*2))
sprites.append(ship_sunk)

# ---turn (40x20)---
ship_turn = pygame.Surface((40, 20)
ship_turn.blit(sprite_sheet, (0, 0), pygame.Rect(SPRITE_WIDTH+SPRITE_MARGIN, SPRITE_HEIGHT*2+SPRITE_MARGIN*2,SPRITE_WIDTH+SPRITE_MARGIN+40, SPRITE_HEIGHT*2+SPRITE_MARGIN*2+20))
sprites.append(ship_turn)

# ---msg_box (250x122)---
ship_msg = pygame.Surface((250, 122)
ship_msg.blit(sprite_sheet, (0, 0), pygame.Rect(0, SPRITE_HEIGHT*3+SPRITE_MARGIN*3, 250, SPRITE_HEIGHT*3+SPRITE_MARGIN*3+122))
sprites.append(ship_msg)

# --------- END YOUR CODE ------------


# set alpha on all sprites to enable transparency
def initialize():
    for sprite in sprites:
        sprite.set_colorkey((255, 0, 255))
        sprite.convert_alpha()