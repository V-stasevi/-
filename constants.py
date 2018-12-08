import pygame
pygame.font.init()

WIDTH = 800
HEIGHT = 600
SIZE = WIDTH, HEIGHT

WIDTH_B = 16*28
HEIGHT_B = 16*30 + 55
SIZE_B = WIDTH_B, HEIGHT_B

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
ORANGE = (255,180,0)
GRAY = 70, 70, 70
YELLOW = 245, 184, 40


POINTS_FOR_SEED = 10
POINTS_FOR_BIGSEED = 100
MATRIX = [[7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 13, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 13],
              [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
              [12, 0, 2, 4, 4, 6, 0, 2, 4, 4, 4, 6, 0, 11, 12, 0, 2, 4, 4, 4, 6, 0, 2, 4, 4, 6, 0, 11],
              [12, 0, 10, 0, 0, 10, 0, 10, 0, 0, 0, 10, 0, 11, 12, 0, 10, 1, 1, 1, 10, 0, 10, 1, 1, 10, 0, 11],
              [12, 0, 3, 4, 4, 8, 0, 3, 4, 4, 4, 8, 0, 20, 21, 0, 3, 4, 4, 4, 8, 0, 3, 4, 4, 8, 0, 11],
              [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
              [12, 0, 2, 4, 4, 6, 0, 2, 6, 0, 2, 4, 4, 4, 4, 4, 4, 6, 0, 2, 6, 0, 2, 4, 4, 6, 0, 11],
              [12, 0, 3, 4, 4, 8, 0, 10, 10, 0, 3, 4, 4, 6, 2, 4, 4, 8, 0, 10, 10, 0, 3, 4, 4, 8, 0, 11],
              [12, 0, 0, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 0, 0, 11],
              [16, 9, 9, 9, 9, 14, 0, 10, 3, 4, 4, 6, 0, 10, 10, 0, 2, 4, 4, 8, 10, 0, 18, 9, 9, 9, 9, 17],
              [0, 0, 0, 0, 0, 12, 0, 10, 2, 4, 4, 8, 0, 3, 8, 0, 3, 4, 4, 6, 10, 0, 11, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 12, 0, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 0, 11, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 12, 0, 10, 10, 0, 2, 4, 4, 0, 0, 4, 4, 6, 0, 10, 10, 0, 11, 0, 0, 0, 0, 0],
              [5, 5, 5, 5, 5, 15, 0, 3, 8, 0, 10, 0, 0, 0, 0, 0, 0, 10, 0, 3, 8, 0, 19, 5, 5, 5, 5, 5],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [9, 9, 9, 9, 9, 14, 0, 2, 6, 0, 10, 0, 0, 0, 0, 0, 0, 10, 0, 2, 6, 0, 18, 9, 9, 9, 9, 9],
              [0, 0, 0, 0, 0, 12, 0, 10, 10, 0, 3, 4, 4, 4, 4, 4, 4, 8, 0, 10, 10, 0, 11, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 12, 0, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 0, 11, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 12, 0, 10, 10, 0, 2, 4, 4, 4, 4, 4, 4, 6, 0, 10, 10, 0, 11, 0, 0, 0, 0, 0],
              [7, 5, 5, 5, 5, 15, 0, 3, 8, 0, 3, 4, 4, 6, 2, 4, 4, 8, 0, 3, 8, 0, 19, 5, 5, 5, 5, 13],
              [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
              [12, 0, 2, 4, 4, 6, 0, 2, 4, 4, 4, 6, 0, 10, 10, 0, 2, 4, 4, 4, 6, 0, 2, 4, 4, 6, 0, 11],
              [12, 0, 3, 4, 6, 10, 0, 3, 4, 4, 4, 8, 0, 3, 8, 0, 3, 4, 4, 4, 8, 0, 10, 2, 4, 8, 0, 11],
              [12, 0, 0, 0, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 0, 0, 0, 11],
              [16, 9, 14, 0, 10, 10, 0, 2, 6, 0, 2, 4, 4, 4, 4, 4, 4, 6, 0, 2, 6, 0, 10, 10, 0, 18, 9, 17],
              [7, 5, 15, 0, 3, 8, 0, 10, 10, 0, 3, 4, 4, 6, 2, 4, 4, 8, 0, 10, 10, 0, 3, 8, 0, 19, 5, 13],
              [12, 0, 0, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 0, 0, 11],
              [12, 0, 2, 4, 4, 4, 4, 8, 3, 4, 4, 6, 0, 10, 10, 0, 2, 4, 4, 8, 3, 4, 4, 4, 4, 6, 0, 11],
              [12, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 8, 0, 3, 8, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 8, 0, 11],
              [12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11],
              [16, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 17],
              ]


ghost_size_x = 15
ghost_size_y = 15

    # ghosts pictures
picGhost_Blinky = pygame.image.load("textures/Ghost-Blinky.png")
picGhost_Blinky = pygame.transform.scale(picGhost_Blinky, (ghost_size_x, ghost_size_y))
picGhost_Clyde = pygame.image.load("textures/Ghost-Clyde.png")
picGhost_Clyde = pygame.transform.scale(picGhost_Clyde, (ghost_size_x, ghost_size_y))
picGhost_Inky = pygame.image.load("textures/Ghost-Inky.png")
picGhost_Inky = pygame.transform.scale(picGhost_Inky, (ghost_size_x, ghost_size_y))
picGhost_Pinky = pygame.image.load("textures/Ghost-pinky.png")
picGhost_Pinky = pygame.transform.scale(picGhost_Pinky, (ghost_size_x, ghost_size_y))
picGhost_Dead = pygame.image.load("textures/Ghost-dead.png")
picGhost_Dead = pygame.transform.scale(picGhost_Dead, (ghost_size_x, ghost_size_y))

    # moving ghosts pictures
picGhost_Blinky_Move = "textures/Ghost-Blinky-move.png"
picGhost_Clyde_Move = "textures/Ghost-Clyde-move.png"
picGhost_Inky_Move = "textures/Ghost-Inky-move.png"
picGhost_Pinky_Move = "textures/Ghost-Pinky-move.png"
picGhost_Dead_Move = "textures/Ghost-dead-move.png"


x_play, y_play = WIDTH/2, HEIGHT/5 * 2
x_records, y_records = WIDTH/2, HEIGHT/5 * 3
x_options, y_options = WIDTH/2, HEIGHT/5 * 4
pic_play, pic_records, pic_options, pic_bg = "textures/Play.png", "textures/Records.png", "textures/Options.png", "textures/Menu.png"
pic_arr = "textures/Ar.png"


BUTTON_STYLE = {
                "font" : pygame.font.SysFont("Alice", 18),
                "hover_color" : GRAY,
                }

right = 0
down = 1
left = 2
up = 3


cherryTexture = "textures/Ghost-Inky.png"
strawberryTexture = "textures/big_seed.png"