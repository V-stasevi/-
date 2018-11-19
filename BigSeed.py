import pygame
from constants import POINTS_FOR_BIGSEED


BigSeed = "img/BigSeed.jpg"

class BigSeed:
    def __init__(self,x, y, pacman_rect):
        self.seed = pygame.image.load(BigSeed)          # Получение картинки
        self.seed_rect.x = x                            #   Получение
        self.seed_rect.y = y                            #   Координат
        self.seed_rect = self.seed.get_rect()
        self.points = constants.POINTS_FOR_BIGSEED      # Количество очков за  большое зерно
        self.Eat = False                            # Изначально зерно не съедено
        self.pacman_rect = pacman_rect

    def eat(self):
        if not self.Eat:
            if self.seed_rect.colliderect(pacman_rect):
                self.Eat = True
                return self.points                      # Добавление очков

    def draw(self, screen):
            if not self.Eat:                        # Eсли зерно ещё не съедено,
            screen.blit(self.seed, self.seed_rect)    # то происходит отрисовка зерна 
