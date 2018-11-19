import pygame

from constants import picGhost_Dead


class Ghost:
    def __init__(self, picture, x, y=30):
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.__update_system_position()
        self.dead = False

    def __update_system_position(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def is_dead(self):
        self.image = pygame.image.load(picGhost_Dead)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        pass

    def check_border(self, window_width, window_height):
        pass

    def logic(self, window_width, window_height):
        self.move()
        self.check_border(window_width, window_height)
        self.__update_system_position()
