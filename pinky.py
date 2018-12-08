from class_ghost import Ghost
from constants import down, up, MATRIX, right, left, picGhost_Pinky, picGhost_Pinky_Move

class Pinky:

    def __init__(self, pacman):
        self.pinky = Ghost(picGhost_Pinky, 15 * 16 - 16)
        self.pacman = pacman

    def now_x(self):
        return int(self.pinky.x/16)

    def now_y(self):
        return int(self.pinky.y/16)

    def check_border_sides(self):
        y = self.now_y()
        x = self.now_x()
        if (x > 11 and x < 18) and (y > 11 and y < 17):
            self.pinky.start()
        else:
            if (self.pinky.direction == up or self.pinky.direction == down) \
                    and (MATRIX[y][x+1] != 0 and MATRIX[y][x-1] != 0):
                self.check_boarder_straight()
            elif (self.pinky.direction == left or self.pinky.direction == right) \
                    and (MATRIX[y+1][x] != 0 and MATRIX[y-1][x] != 0):
                self.check_boarder_straight()

            else:
                self.turn()

    def check_boarder_straight(self):
        y = self.now_y()
        x = self.now_x()
        if (self.pinky.direction == up and MATRIX[y-1][x] != 0) \
                or (self.pinky.direction == down and MATRIX[y+1][x] != 0) \
                or (self.pinky.direction == right and MATRIX[y][x+1] != 0) \
                or (self.pinky.direction == left and MATRIX[y][x-1] != 0):
            if ((self.pinky.direction == up or self.pinky.direction == down) and y != int(self.pacman.y/16)) \
                    or ((self.pinky.direction == left or self.pinky.direction == right) and x != int(self.pacman.x/16)):
                self.turn()
        else:
            self.pinky.move_straight()

    def set_speed(self, new_speed):
        self.pinky.speed = new_speed

    # def state(self):
    #     pass

    def turn(self):
        y = self.now_y()
        x = self.now_x()
        if self.pinky.direction == up or self.pinky.direction == down:
            if MATRIX[y][x-1] != 0:
                self.pinky.direction = right
            elif MATRIX[y][x+1] != 0:
                self.pinky.direction = left
            else:
                turn_left = abs(self.pacman.x + 4*16 - self.pinky.x - 16)
                turn_right = abs(self.pacman.x + 4*16 - self.pinky.x + 16)
                if turn_left >= turn_right:
                    self.pinky.direction = left
                else:
                    self.pinky.direction = right

        elif self.pinky.direction == right or self.pinky.direction == left:
            if MATRIX[y-1][x] != 0:
                self.pinky.direction = down
            elif MATRIX[y+1][x] != 0:
                self.pinky.direction = up
            else:
                turn_up = abs(self.pacman.y + 4*16 - self.pinky.y - 16)
                turn_down = abs(self.pacman.y + 4*16 - self.pinky.y + 16)
                if turn_up >= turn_down:
                    self.pinky.direction = up
                else:
                    self.pinky.direction = down
        self.pinky.move_straight()

    def move(self):
        self.check_border_sides()
        self.__update_system_position()

    def __update_system_position(self):
        self.pinky.rect.x = self.pinky.x
        self.pinky.rect.y = self.pinky.y

    def draw(self, screen):
        screen.blit(self.pinky.image, self.pinky.rect)

    # def image_loop(self):
    #     if self.pinky.image == picGhost_Pinky:
    #         self.pinky.image == picGhost_Pinky_Move
    #     else:
    #         self.pinky.image == picGhost_Pinky
