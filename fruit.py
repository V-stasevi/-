import pygame

cherryTexture = "images/cherry"
strawberryTexture = "images/strawberry"


class Cherry:
    def __init__(self, x, y, pacman_rect):
        self.image = pygame.image.load(cherryTexure)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_eaten = False
        self.points = 100        # Кол-во очков
        self.pacman_rect = pacman_rect

    def eat(self):
        if not self.is_eaten and self.rect.colliderect(pacman_rect):
            self.is_eaten = True
            return self.points


class Strawberry(Cherry):
    def __init__(self, x, y, pacman_rect):
        super().__init__(self, x, y, pacman_rect)
        self.image = pygame.image.load(strawberryTexture)
        self.points = 300  # Кол-во очков
