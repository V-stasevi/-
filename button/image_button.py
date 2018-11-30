from button import Button
import pygame
from constants import WHITE

class ImageButton(Button):

    background = "button/wheel.png"

    def __init__(self, x, y, function_begin, function_end):
        self.image = pygame.image.load(self.background)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.function_on_start = function_begin
        self.function_on_end = function_end
        self.clicked = False

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("yes")


    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            if not self.clicked:
                self.clicked = True
                self.function_on_start()
            else:
                self.function_on_end()
                self.clicked = False


    def update(self, surface):
        surface.blit(self.image, self.rect)



