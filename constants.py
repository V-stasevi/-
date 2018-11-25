WIDTH = 800
HEIGHT = 600
SIZE = WIDTH, HEIGHT
BLACK = 0, 0, 0
WHITE = 255, 255, 255
POINTS_FOR_SEED = 10
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




    # ghosts pictures
picGhost_Blinky = "images/Ghost-Blinky.png"
picGhost_Clyde = "images/Ghost-Clyde.png"
picGhost_Inky = "images/Ghost-Inky.png"
picGhost_Pinky = "images/Ghost-Pinky.png"
picGhost_Dead = "images/Ghost-dead.png"

    # moving ghosts pictures
picGhost_Blinky_Move = "images/Ghost-Blinky-move.png"
picGhost_Clyde_Move = "images/Ghost-Clyde-move.png"
picGhost_Inky_Move = "images/Ghost-Inky-move.png"
picGhost_Pinky_Move = "images/Ghost-Pinky-move.png"
picGhost_Dead_Move = "images/Ghost-dead-move.png"

