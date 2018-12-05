import pygame
from random import randint
from constants import WIDTH, HEIGHT, WHITE

class Text:
    def __init__(self, x, y, text='Hello, Pygame!',
                 font="Comic Sans MS", size=35, color=WHITE, bold=True, italic=False):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.size = size
        self.color = color
        self.bold = bold
        self.italic = italic
        self.font_object = pygame.font.SysFont(self.font, self.size, self.bold, self.italic)
        self.text_surface = self.font_object.render(self.text, True, self.color)
        self.rect = self.text_surface.get_rect()

    def updateText(self, newText):
        self.text = newText
        self.text_surface = self.font_object.render(self.text, False, self.color)
    def draw(self, screen):
        screen.blit(self.text_surface, (int(self.x), int(self.y)))
