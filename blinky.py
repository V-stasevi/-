from class_ghost import Ghost
from constants import picGhost_Blinky, picGhost_Blinky_Move, MATRIX, up, down, right, left

class Blinky:

    def __init__(self, pacman):

        self.image = picGhost_Blinky
        self.blinky = Ghost(self.image, 15 * 16 - 20)
        self.direction = down
        self.pacman = pacman
        self.speed = 16

    def check_boarder(self):
        y = int(self.blinky.y/16)
        x = int(self.blinky.x/16)
        if (self.direction == up and MATRIX[y+1][x] != 0) \
                or (self.direction == down and MATRIX[y-1][x] != 0) \
                or (self.direction == right and MATRIX[y][x+1] != 0) \
                or (self.direction == left and MATRIX[y][x-1] != 0):
            return False
        else:
            return True

    def set_speed(self, new_speed):
        self.speed = new_speed

    def state(self):
        pass

    def turn(self):
        if self.check_boarder() == 0:
            if self.direction == up or self.direction == down:

                turn_left = abs(self.pacman.x - self.blinky.x - 16)
                turn_right = abs(self.pacman.x - self.blinky.x + 16)
                if turn_left <= turn_right:
                    self.direction = left
                else:
                    self.direction = right

            elif self.direction == right or self.direction == left:

                turn_up = abs(self.pacman.y - self.blinky.y + 16)
                turn_down = abs(self.pacman.y - self.blinky.y - 16)
                if turn_up <= turn_down:
                    self.direction = up
                else:
                    self.direction = down

    def move_straight(self):
        if self.direction == up:
            self.blinky.y += self.speed
        elif self.direction == down:
            self.blinky.y -= self.speed
        elif self.direction == right:
            self.blinky.x += self.speed
        elif self.direction == left:
            self.blinky.x -= self.speed

    def move(self):
        if self.check_boarder():
            self.move_straight()
        elif self.check_boarder() == 0:
            self.turn()

    def draw(self, screen):
        screen.blit(self.blinky.image, self.blinky.rect)

    def image_loop(self):
        if self.blinky.image == picGhost_Blinky:
            self.blinky.image == picGhost_Blinky_Move
        else:
            self.blinky.image == picGhost_Blinky


