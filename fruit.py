import pygame

from constants import cherryTexture, strawberryTexture


class Cherry:
    def __init__(self, x, y):
        self.image = pygame.image.load(cherryTexture)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_eaten = False
        self.points = 100        # Кол-во очков

    def eat(self, pacman_rect):
        if not self.is_eaten and self.rect.colliderect(pacman_rect):
            self.is_eaten = True
            return self.points

    def draw(self, screen):
        if not self.is_eaten:
            screen.blit(self.image, self.rect)


class Strawberry(Cherry):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load(strawberryTexture)
        self.points = 300  # Кол-во очков
