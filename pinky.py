from class_ghost import Ghost
from constants import down, up, MATRIX, right, left, picGhost_Pinky, picGhost_Pinky_Move


class Pinky:

    def __init__(self, pacman):
        self.pinky = Ghost(picGhost_Pinky, 15 * 16 - 16)
        self.direction = up
        self.pacman = pacman
        self.speed = 16

    def now_x(self):
        return int(self.pinky.x/16)

    def now_y(self):
        return int(self.pinky.y/16)

    def check_border_sides(self):
        y = self.now_y()
        x = self.now_x()
        if (self.direction == up or self.direction == down) \
                and (MATRIX[y][x+1] != 0 and MATRIX[y][x-1] != 0):
            self.check_boarder_straight()
        elif (self.direction == left or self.direction == right) \
                and (MATRIX[y+1][x] != 0 and MATRIX[y-1][x] != 0):
            self.check_boarder_straight()

        else:
            self.turn()

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

    def set_speed(self, new_speed):
        self.speed = new_speed

    def eat(self):
        pass

    def death(self):
        pass

    def state(self):
        pass

    def turn(self):
        y = self.now_y()
        x = self.now_x()
        if self.direction == up or self.direction == down:
            if MATRIX[y][x-1] != 0:
                self.direction = right
            elif MATRIX[y][x+1] != 0:
                self.direction = left
            else:
                turn_left = abs(self.pacman.x + 4*16 - self.pinky.x - 16)
                turn_right = abs(self.pacman.x + 4*16 - self.pinky.x + 16)
                if turn_left <= turn_right:
                    self.direction = left
                else:
                    self.direction = right

        elif self.direction == right or self.direction == left:
            if MATRIX[y-1][x] != 0:
                self.direction = down
            elif MATRIX[y+1][x] != 0:
                self.direction = up
            else:
                turn_up = abs(self.pacman.y + 4*16 - self.pinky.y - 16)
                turn_down = abs(self.pacman.y + 4*16 - self.pinky.y + 16)
                if turn_up >= turn_down:
                    self.direction = up
                else:
                    self.direction = down

    def move_straight(self):
        if self.direction == up:
            self.pinky.y -= self.speed
        elif self.direction == down:
            self.pinky.y += self.speed
        elif self.direction == right:
            self.pinky.x += self.speed
        elif self.direction == left:
            self.pinky.x -= self.speed

    def move(self):
        if self.check_boarder_straight():
            self.move_straight()
        elif self.check_boarder_straight() == 0:
            self.turn()
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

    # def check_b2(self):
    #     y = self.now_y()
    #     x = self.now_x()
    #
    #     if self.direction == up and MATRIX[y - 1][x] != 0:
    #         self.direction = right
    #     elif self.direction == right and MATRIX[y][x+1] != 0:
    #         self.direction = down
    #     elif self.direction == down and MATRIX[y+1][x] != 0:
    #         self.direction = left
    #     elif self.direction == left and MATRIX[y][x-1] != 0:
    #         self.direction = up

    # def angle_left_up(self):
    #     if self.direction == left:
    #         self.direction = down
    #     else:
    #         self.direction = right
    #
    # def angle_right_up(self):
    #     if self.direction == right:
    #         self.direction = down
    #     else:
    #         self.direction = left
    #
    # def angle_left_down(self):
    #     if self.direction == left:
    #         self.direction = up
    #     else:
    #         self.direction = right
    #
    # def angle_right_down(self):
    #     if self.direction == right:
    #         self.direction = up
    #     else:
    #         self.direction = left
    #
    # def angle_turn(self):
    #     y = self.now_y()
    #     x = self.now_x()

    # left_up_angle = [{2, 2}, {16, 2}, {16, 9}, {10, 12}, {2, 21},
    #                {16, 21}, {25, 24}, {2, 27}, {16, 27}]
    # right_up_angle = [{13, 2}, {27, 2}, {13, 9}, {19, 12}, {13, 21},
    #                   {27, 21}, {4, 24}, {13, 27}, {27, 27}]
    # left_down_angle = [{2, 9}, {10, 9}, {2, 24}, {10, 27}, {22, 27},
    #                    {2, 30}]
    # right_down_angle = [{19, 9}, {27, 9}, {27, 24}, {19, 27}, {27, 30}]
    #
    # angle_y = [2, 9, 13, 21, 24, 27, 30]

    # if y == 2 or y == 21:
    #     if x == 27 or x == 13:
    #         self.angle_right_up()
    #     elif x == 2 or x == 16:
    #         self.angle_left_up()
    #
    # elif y == 9:
    #     if x == 2 or x == 10:
    #         self.angle_left_down()
    #     elif x == 13:
    #         self.angle_right_up()
    #     elif x == 19 or x == 27:
    #         self.angle_right_down()
    #     elif x == 16:
    #         self.angle_left_up()
    #
    # elif y == 13:
    #     if x == 10:
    #         self.angle_left_up()
    #     elif x == 19:
    #         self.angle_right_up()
    #
    # elif y == 24:
    #     if x == 2:
    #         self.angle_left_down()
    #     elif x == 4:
    #         self.angle_right_up()
    #     elif x == 25:
    #         self.angle_left_up()
    #     elif x == 27:
    #         self.angle_right_down()
    #
    # elif y == 27:
    #     if x == 2 or x == 16:
    #         self.angle_left_up()
    #     elif x == 7 or x == 19:
    #         self.angle_right_down()
    #     elif x == 10 or x == 22:
    #         self.angle_left_down()
    #     elif x == 13 or x == 27:
    #         self.angle_right_up()
    #
    # elif y == 30:
    #     if x == 2:
    #         self.angle_left_down()
    #     elif x == 27:
    #         self.angle_right_down()
    #
    #
    # for e in angle_y:
    #     if y == e:
    #         if {x, y} == 0:
    #             pass
    #
    # for elem in left_up_angle:
    #     if elem == {x, y}:
    #         self.angle_left_up()
    # for elem in left_down_angle:
    #     if elem == {x, y}:
    #         self.angle_left_down()
    # for elem in right_up_angle:
    #     if elem == {x, y}:
    #         self.angle_right_up()
    # for elem in right_down_angle:
    #     if elem == {x, y}:
    #         self.angle_right_down()