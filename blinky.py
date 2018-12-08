from class_ghost import Ghost
from constants import picGhost_Blinky, picGhost_Blinky_Move, MATRIX, up, down, right, left

class Blinky:

    def __init__(self, pacman):
        self.blinky = Ghost(picGhost_Blinky, 15 * 16 - 32)
        self.pacman = pacman

    def now_x(self):
        return int(self.blinky.x / 16)

    def now_y(self):
        return int(self.blinky.y / 16)

    def check_border_sides(self):
        y = self.now_y()
        x = self.now_x()
        if (x > 11 and x < 18) and (y > 11 and y < 17):
            self.blinky.start()
        else:
            if (self.blinky.direction == up or self.blinky.direction == down) \
                    and (MATRIX[y][x+1] != 0 and MATRIX[y][x-1] != 0):
                self.check_boarder_straight()
            elif (self.blinky.direction == left or self.blinky.direction == right) \
                    and (MATRIX[y+1][x] != 0 and MATRIX[y-1][x] != 0):
                self.check_boarder_straight()

            else:
                self.turn()

    def check_boarder_straight(self):
        y = self.now_y()
        x = self.now_x()
        if (self.blinky.direction == up and MATRIX[y-1][x] != 0) \
                or (self.blinky.direction == down and MATRIX[y+1][x] != 0) \
                or (self.blinky.direction == right and MATRIX[y][x+1] != 0) \
                or (self.blinky.direction == left and MATRIX[y][x-1] != 0):
            if ((self.blinky.direction == up or self.blinky.direction == down) and y != int(self.pacman.y/16)) \
                    or ((self.blinky.direction == left or self.blinky.direction == right) and x != int(self.pacman.x/16)):
                self.turn()
        else:
            self.blinky.move_straight()

    def set_speed(self, new_speed):
        self.blinky.speed = new_speed

    # def state(self):
    #     pass

    def turn(self):
        y = self.now_y()
        x = self.now_x()
        if self.blinky.direction == up or self.blinky.direction == down:
            if MATRIX[y][x-1] != 0:
                self.blinky.direction = right
            elif MATRIX[y][x+1] != 0:
                self.blinky.direction = left
            else:
                turn_left = abs(self.pacman.x - self.blinky.x - 16)
                turn_right = abs(self.pacman.x - self.blinky.x + 16)
                if turn_left >= turn_right:
                    self.blinky.direction = left
                else:
                    self.blinky.direction = right

        elif self.blinky.direction == right or self.blinky.direction == left:
            if MATRIX[y-1][x] != 0:
                self.blinky.direction = down
            elif MATRIX[y+1][x] != 0:
                self.blinky.direction = up
            else:
                turn_up = abs(self.pacman.y - self.blinky.y - 16)
                turn_down = abs(self.pacman.y - self.blinky.y + 16)
                if turn_up >= turn_down:
                    self.blinky.direction = up
                else:
                    self.blinky.direction = down
        self.blinky.move_straight()

    def move(self):
        self.check_border_sides()
        self.__update_system_position()

    def __update_system_position(self):
        self.blinky.rect.x = self.blinky.x
        self.blinky.rect.y = self.blinky.y

    def draw(self, screen):
        screen.blit(self.blinky.image, self.blinky.rect)

    # def image_loop(self):
    #     if self.blinky.image == picGhost_Blinky:
    #         self.blinky.image == picGhost_Blinky_Move
    #     else:
    #         self.blinky.image == picGhost_Blinky
