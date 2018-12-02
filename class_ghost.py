import pygame
from constants import picGhost_Dead

common = True

class Ghost:
    def __init__(self, picture, x):
        self.image = picture
        self.rect = self.image.get_rect()
        self.x = x
        self.y = 15*16
        self.state = common
        self.__update_system_position()
        self.dead = False

    def __update_system_position(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def is_dead(self):
        self.image = pygame.image.load(picGhost_Dead)

    def move(self):
        pass

    def check_border(self, window_width, window_height):
        pass

    def logic(self, window_width, window_height):

        self.__update_system_position()

