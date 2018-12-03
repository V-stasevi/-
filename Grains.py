import pygame, constants

"""
Здесь сразу два класса. 1 - smallGrain, при создании передается два параметра x, y, а так же передается Rect пакмана. За отрисовку отвечает метод draw(), 
при вызове передается дисплей куда отрисовывать. eat() - проверяет съедено ли зерно
eat() - лучше вызывать в process_logic

2 - energizer.
Класс наследник от smallGrain. eat заменен на eatEnergizer(). Так же необходимо прописать, что делать при съедании
"""

# НЕ ЗАБУДЬ ПОМЕНЯТЬ ТЕКСТУРКИ НА НОРМАЛЬНЫЕ

smallSeedTexture = "textures/small_seed.png"
energizerTexture = "textures/big_seed.png"


class smallGrain:
    def __init__(self,x, y):
        self.grain = pygame.image.load(smallSeedTexture)
        self.grain_rect = self.grain.get_rect()
        self.points = constants.POINTS_FOR_SEED
        self.grain_rect.x = x + 2
        self.grain_rect.y = y + 2
        self.isEaten = False

    def eat(self, pacman_rect):
        if not self.isEaten:
            if pacman_rect.colliderect(self.grain_rect):
                print(True)
                self.isEaten = True    # Добавление очков, так же можно потом переделать.
            else:
                print(False)


    def draw(self, screen):
        if self.isEaten:
            pass
        else:
            screen.blit(self.grain, self.grain_rect)

class enegrizer(smallGrain):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.grain = pygame.image.load(energizerTexture)

    def eatEnergizer(self):
        if not self.isEaten:
            if self.grain_rect.colliderect():
                pass                                # Activate energizer here