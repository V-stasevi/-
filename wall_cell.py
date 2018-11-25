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
        elif self.cell_type == 5:
            pygame.gfxdraw.line(surface, self.x, self.y + 4, self.x + 16, self.y + 4, self.color)
            pygame.gfxdraw.line(surface, self.x, self.y + 8, self.x + 16, self.y + 8, self.color)
        elif self.cell_type == 6:
            pygame.gfxdraw.arc(surface, self.x, self.y+16, 8, 270, 0, self.color)
        elif self.cell_type == 7:
            pygame.gfxdraw.arc(surface, self.x + 16, self.y + 16, 12, 180, 270, self.color)
            pygame.gfxdraw.arc(surface, self.x + 16, self.y + 16, 8, 180, 270, self.color)
        elif self.cell_type == 8:
            pygame.gfxdraw.arc(surface, self.x, self.y, 8, 0, 90, self.color)
        elif self.cell_type == 9:
            pygame.gfxdraw.line(surface, self.x, self.y + 8, self.x + 16, self.y + 8, self.color)
            pygame.gfxdraw.line(surface, self.x, self.y + 12, self.x + 16, self.y + 12, self.color)
        elif self.cell_type == 10:
            pygame.gfxdraw.line(surface, self.x+8, self.y, self.x+8, self.y +16, self.color)
        elif self.cell_type == 11:
            pygame.gfxdraw.line(surface, self.x+8, self.y, self.x+8, self.y +16, self.color)
            pygame.gfxdraw.line(surface, self.x + 12, self.y, self.x + 12, self.y + 16, self.color)
        elif self.cell_type == 12:
            pygame.gfxdraw.line(surface, self.x + 4, self.y, self.x + 4, self.y + 16, self.color)
            pygame.gfxdraw.line(surface, self.x+8, self.y, self.x+8, self.y +16, self.color)
        elif self.cell_type == 13:
            pygame.gfxdraw.arc(surface, self.x, self.y + 16, 12, 270, 0, self.color)
            pygame.gfxdraw.arc(surface, self.x, self.y + 16, 8, 270, 0, self.color)
        elif self.cell_type == 14:
            pygame.gfxdraw.arc(surface, self.x, self.y+16, 8, 270, 0, self.color)
            pygame.gfxdraw.arc(surface, self.x, self.y + 16, 4, 270, 0, self.color)
        elif self.cell_type == 15:
            pygame.gfxdraw.arc(surface, self.x, self.y, 4, 0, 90, self.color)
            pygame.gfxdraw.arc(surface, self.x, self.y, 8, 0, 90, self.color)
        elif self.cell_type == 16:
            pygame.gfxdraw.arc(surface, self.x+16, self.y, 8, 90, 180, self.color)
            pygame.gfxdraw.arc(surface, self.x + 16, self.y, 12, 90, 180, self.color)
        elif self.cell_type == 17:
            pygame.gfxdraw.arc(surface, self.x, self.y, 8, 0, 90, self.color)
            pygame.gfxdraw.arc(surface, self.x, self.y, 12, 0, 90, self.color)
        elif self.cell_type == 18:
            pygame.gfxdraw.arc(surface, self.x + 16, self.y + 16, 4, 180, 270, self.color)
            pygame.gfxdraw.arc(surface, self.x + 16, self.y + 16, 8, 180, 270, self.color)
        elif self.cell_type == 19:
            pygame.gfxdraw.arc(surface, self.x + 16, self.y, 4, 90, 180, self.color)
            pygame.gfxdraw.arc(surface, self.x+16, self.y, 8, 90, 180, self.color)
        elif self.cell_type == 20:
            pygame.gfxdraw.arc(surface, self.x + 16, self.y, 4, 90, 180, self.color)
            pygame.gfxdraw.arc(surface, self.x+16, self.y, 8, 90, 180, self.color)
        elif self.cell_type == 21:
            pygame.gfxdraw.arc(surface, self.x, self.y, 4, 0, 90, self.color)
            pygame.gfxdraw.arc(surface, self.x, self.y, 8, 0, 90, self.color)
