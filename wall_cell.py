from cell import Cell


class WallCell(Cell):
    def __init__(self, x, y, cell_size):
        Cell.__init__(self, x, y, cell_size)
        self.color = 70, 130, 180
        self.fill = 0
        self.walkable = False
