from cell import Cell
from wall_cell import WallCell


# размер 31х28
class Field:
    h_cells = 28
    v_cells = 31

    # matrix = [[None for _ in range(35)] for _ in range(27)]
    matrix = [[2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6],
              [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
              [10, 0, 2, 4, 4, 6, 0, 2, 4, 4, 4, 6, 0, 10, 10, 0, 2, 4, 4, 4, 6, 0, 2, 4, 4, 6, 0, 10],
              [10, 0, 10, 0, 0, 10, 0, 10, 0, 0, 0, 10, 0, 10, 10, 0, 10, 1, 1, 1, 10, 0, 10, 1, 1, 10, 0, 10],
              [10, 0, 3, 4, 4, 8, 0, 3, 4, 4, 4, 8, 0, 3, 8, 0, 3, 4, 4, 4, 8, 0, 3, 4, 4, 8, 0, 10],
              [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
              [10, 0, 2, 4, 4, 6, 0, 2, 6, 0, 2, 4, 4, 4, 4, 4, 4, 6, 0, 2, 6, 0, 2, 4, 4, 6, 0, 10],
              [10, 0, 3, 4, 4, 8, 0, 10, 10, 0, 3, 4, 4, 6, 2, 4, 4, 8, 0, 10, 10, 0, 3, 4, 4, 8, 0, 10],
              [10, 0, 0, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 0, 0, 10],
              [3, 4, 4, 4, 4, 6, 0, 10, 3, 4, 4, 6, 0, 10, 10, 0, 2, 4, 4, 8, 10, 0, 2, 4, 4, 4, 4, 8],
              [0, 0, 0, 0, 0, 10, 0, 10, 2, 4, 4, 8, 0, 3, 8, 0, 3, 4, 4, 6, 10, 0, 10, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 10, 0, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 0, 10, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 10, 0, 10, 10, 0, 2, 4, 4, 0, 0, 4, 4, 6, 0, 10, 10, 0, 10, 0, 0, 0, 0, 0],
              [4, 4, 4, 4, 4, 8, 0, 3, 8, 0, 10, 0, 0, 0, 0, 0, 0, 10, 0, 3, 8, 0, 3, 4, 4, 4, 4, 4],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [4, 4, 4, 4, 4, 6, 0, 2, 6, 0, 10, 0, 0, 0, 0, 0, 0, 10, 0, 2, 6, 0, 2, 4, 4, 4, 4, 4],
              [0, 0, 0, 0, 0, 10, 0, 10, 10, 0, 3, 4, 4, 4, 4, 4, 4, 8, 0, 10, 10, 0, 10, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 10, 0, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 0, 10, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 10, 0, 10, 10, 0, 2, 4, 4, 4, 4, 4, 4, 6, 0, 10, 10, 0, 10, 0, 0, 0, 0, 0],
              [2, 4, 4, 4, 4, 8, 0, 3, 8, 0, 3, 4, 4, 6, 2, 4, 4, 8, 0, 3, 8, 0, 3, 4, 4, 4, 4, 6],
              [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
              [10, 0, 2, 4, 4, 6, 0, 2, 4, 4, 4, 6, 0, 10, 10, 0, 2, 4, 4, 6, 1, 0, 2, 4, 4, 6, 0, 10],
              [10, 0, 3, 4, 6, 10, 0, 3, 4, 4, 4, 8, 0, 3, 8, 0, 3, 4, 4, 8, 1, 0, 10, 2, 4, 8, 0, 10],
              [10, 0, 0, 0, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 0, 0, 0, 10],
              [3, 4, 6, 0, 10, 10, 0, 2, 6, 0, 2, 4, 4, 4, 4, 4, 4, 6, 0, 2, 6, 0, 10, 10, 0, 2, 4, 8],
              [2, 4, 8, 0, 3, 8, 0, 10, 10, 0, 3, 4, 4, 6, 2, 4, 4, 8, 0, 10, 10, 0, 3, 8, 0, 3, 4, 6],
              [10, 0, 0, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 10, 10, 0, 0, 0, 0, 0, 0, 10],
              [10, 0, 2, 4, 4, 4, 4, 8, 3, 4, 4, 6, 0, 10, 10, 0, 2, 4, 4, 8, 3, 4, 4, 4, 4, 6, 0, 10],
              [10, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 8, 0, 3, 8, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 8, 0, 10],
              [10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
              [3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8],
              ]

    def __init__(self, x, y, cell_size=16):
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.matrix = self.__create_matrix()

    def __create_matrix(self):
        for i in range(self.v_cells):
            for j in range(self.h_cells):
                if self.matrix[i][j] == 1:
                    type = self.matrix[i][j]
                    cell_x = self.x + j + j * self.cell_size
                    cell_y = self.y + i + i * self.cell_size
                    cell = WallCell(cell_x, cell_y, self.cell_size, type)
                elif self.matrix[i][j] == 0:
                    cell_x = self.x + j + j * self.cell_size
                    cell_y = self.y + i + i * self.cell_size
                    cell = Cell(cell_x, cell_y, self.cell_size)
                else:
                    type = self.matrix[i][j]
                    cell_x = self.x + j + j * self.cell_size
                    cell_y = self.y + i + i * self.cell_size
                    cell = WallCell(cell_x, cell_y, self.cell_size, type)

                self.matrix[i][j] = cell
        return self.matrix

    def draw(self, surface):
        for i in range(self.v_cells):
            for j in range(self.h_cells):
                self.matrix[i][j].draw(surface)
