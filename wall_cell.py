from cell import Cell
import pygame
import pygame.gfxdraw


class WallCell(Cell):
    def __init__(self, x, y, cell_size, cell_type):
        Cell.__init__(self, x, y, cell_size)
        self.color = 30, 144, 255
        self.fill = 2
        self.walkable = False
        self.cell_type = cell_type


    def draw(self, surface):

        if self.cell_type == 2:
            pygame.gfxdraw.arc(surface, self.x + 16, self.y+16, 8, 180, 270, self.color)
        elif self.cell_type == 3:
            pygame.gfxdraw.arc(surface, self.x+16, self.y, 8, 90, 180, self.color)
        elif self.cell_type == 4:
            pygame.gfxdraw.line(surface, self.x, self.y+8, self.x+16, self.y+8, self.color)
        elif self.cell_type == 6:
            pygame.gfxdraw.arc(surface, self.x, self.y+16, 8, 270, 0, self.color)
        elif self.cell_type == 8:
            pygame.gfxdraw.arc(surface, self.x, self.y, 8, 0, 90, self.color)
        elif self.cell_type == 10:
            pygame.gfxdraw.line(surface, self.x+8, self.y, self.x+8, self.y +16, self.color)



