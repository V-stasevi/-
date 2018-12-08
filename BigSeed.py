import pygame
from constants import POINTS_FOR_BIGSEED


bigSeedTexture = "textures/big_seed.png"

class BigSeed:
    def __init__(self,x, y):
        self.seed = pygame.image.load(bigSeedTexture)          # Получение картинки
        self.seed_rect = self.seed.get_rect()
        self.seed_rect.x = x
        self.seed_rect.y = y
        self.is_eaten = False                            # Изначально зерно не съедено

    def draw(self, screen):
        if not self.is_eaten:                        # Eсли зерно ещё не съедено,
            screen.blit(self.seed, self.seed_rect)    # то происходит отрисовка зерна
