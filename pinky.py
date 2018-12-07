from class_ghost import Ghost
from constants import down, up, MATRIX, right, left, picGhost_Pinky, picGhost_Pinky_Move


class Pinky:

    def __init__(self, pacman):
        self.pinky = Ghost(picGhost_Pinky, 15 * 16 - 16)
        self.direction = up
        self.pacman = pacman
        self.speed = 16

    def check_boarder(self):
        y = int(self.pinky.y/16)
        x = int(self.pinky.x/16)
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

        if self.direction == up or self.direction == down:

            turn_left = abs(self.pacman.x + 4 - self.pinky.x - 16)
            turn_right = abs(self.pacman.x + 4 - self.pinky.x + 16)
            if turn_left <= turn_right:
                self.direction = left
            else:
                self.direction = right

        elif self.direction == right or self.direction == left:

            turn_up = abs(self.pacman.y + 4 - self.pinky.y - 16)
            turn_down = abs(self.pacman.y + 4 - self.pinky.y + 16)
            if turn_up <= turn_down:
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
        if self.check_boarder():
            self.move_straight()
        elif self.check_boarder() == 0:
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