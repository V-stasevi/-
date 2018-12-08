import pygame
from Grains import smallGrain
from fruit import Cherry, Strawberry

class Cell:

    def __init__(self, x, y, cell_size=16):
        self.x = x
        self.y = y
        self.color = 0,0,0
        self.fill = 0
        self.walkable = True
        self.cell_size = cell_size
        self.width = cell_size
        self.height = cell_size
        self.grain = smallGrain(self.x, self.y)
        self.cherry = Cherry(self.x, self.y)
        self.srawberry = Strawberry(self.x, self.y)
        self.isFruit = False
        self.fruitCount = 0

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height), self.fill)
        if not self.isFruit:
            self.grain.draw(surface)
        elif self.fruitCount == 0:
            self.cherry.draw(surface)
        elif self.fruitCount == 1:
            self.srawberry.draw(surface)

        #print("drawing individual cell")
