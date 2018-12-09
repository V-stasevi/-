import pygame
from text import Text
from constants import WHITE, HEIGHT_B, POINTS_FOR_SEED


class Score:
    def __init__(self, x, y, screen, matrix):
        self.count = 0
        self.countGhost = 1
        self.points = 0
        self.scoreText = Text(x, HEIGHT_B - y, "Score: " + str(self.points))
        self.screen = screen
        self.matrix = matrix

    def checkScore(self):
        if self.count == 70:
            self.matrix.matrix[22][12].isFruit = True
            self.matrix.matrix[22][12].fruitCount += 1
            self.matrix.matrix[6][6].fruitCount += 1
            self.count += 1
        if self.count == 170:
            self.count += 1
            self.matrix.matrix[6][6].isFruit = True

    def logic(self):
        self.points += POINTS_FOR_SEED
        self.count += 1
        self.checkScore()

    def addGhostPoints(self):
        self.points += 400*self.countGhost

    def draw(self):
        self.scoreText.updateText("Score: " + str(self.points))
        self.scoreText.draw(self.screen)