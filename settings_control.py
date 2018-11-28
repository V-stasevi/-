from button  import Button
import pygame
from constants import HEIGHT, WIDTH


class Control:
    def __init__(self):
        self.waiting = True
        self.control_height = HEIGHT//2
        self.control_width = WIDTH // 2
        self.screen = pygame.display.set_mode(self.control_height, self.control_width)


    def main_loop(self):
        while waiting:
            pass
