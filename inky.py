import pygame

from class_ghost import Ghost
from constants import picGhost_Inky, left, up, down, right, MATRIX


class Inky(Ghost):
    def __init__(self, matrix):
        super().__init__(picGhost_Inky, 13*16)
        self.matrix = matrix
        self.directions = []
        self.end_point = matrix[0][0]
        self.acc_pos = matrix[self.y//16][self.x//16]

    def now_x(self):
        return int(self.x / 16)

    def now_y(self):
        return int(self.y / 16)

    def turn(self, pacman):
        y = self.now_y()
        x = self.now_x()
        if self.direction == up or self.direction == down:
            if MATRIX[y][x - 1] != 0:
                self.direction = right
            elif MATRIX[y][x + 1] != 0:
                self.direction = left
            else:
                turn_left = abs((pacman.rect.x+32)  - self.x)
                turn_right = abs((pacman.x-32) - self.x)
                if turn_left <= turn_right:
                    self.direction = left
                else:
                    self.direction = right

        elif self.direction == right or self.direction == left:
            if MATRIX[y - 1][x] != 0:
                self.direction = down
            elif MATRIX[y + 1][x] != 0:
                self.direction = up
            else:
                turn_up = abs((pacman.rect.y + 32) - self.y)
                turn_down = abs((pacman.y - 32) - self.y)
                if turn_up >= turn_down:
                    self.direction = up
                else:
                    self.direction = down
        self.move_straight()

    def check_boarder_straight(self):
        y = self.now_y()
        x = self.now_x()
        if (self.direction == up and MATRIX[y-1][x] != 0) \
                or (self.direction == down and MATRIX[y+1][x] != 0) \
                or (self.direction == right and MATRIX[y][x+1] != 0) \
                or (self.direction == left and MATRIX[y][x-1] != 0):
            return False
        else:
            return True

    def __update_system_position(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def moveInky(self, pacman, score):
        if self.check_boarder_straight():
            self.move_straight()
        elif self.check_boarder_straight() == 0:
            self.turn(pacman)

        self.collision(pacman, score)
        self.__update_system_position()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def process_logic(self, pacman, score):
        self.moveInky(pacman, score)