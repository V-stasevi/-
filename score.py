import pygame
from text import Text
from constants import WHITE, HEIGHT_B

class Score:
    def __init__(self, x, y, screen):
        self.pointsGrains = 0
        self.scoreText = Text(x, HEIGHT_B - y, "Score: " + str(self.pointsGrains))
        self.screen = screen

    def draw(self):
        self.scoreText.updateText("Score: " + str(self.pointsGrains))
        self.scoreText.draw(self.screen)